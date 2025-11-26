#!/usr/bin/env python3
import xrpl
from xrpl.core import addresscodec

# ---------------------------------------
# USER INPUT
# ---------------------------------------
SEED_TEMPLATE = "sEdXXXXXXXXXXXXXXXXXXXXXX?XXX"  # put your seed with ? at pos 27
UNKNOWN_POS = 27  # 1-based index of '?'

KNOWN_PUBLIC_KEY = "EDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # your actual public key
KNOWN_ADDRESS = "rXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"     # your actual address

# Only two candidates
CANDIDATES = ["m", "n"]

# Try both Ed25519 and Secp256k1
ALGORITHMS = ["ed25519", "secp256k1"]

print("[+] Starting 2-option brute force...\n")

for c in CANDIDATES:
    seed_list = list(SEED_TEMPLATE)
    seed_list[UNKNOWN_POS - 1] = c
    candidate_seed = "".join(seed_list)

    for algo in ALGORITHMS:
        try:
            kp = xrpl.core.keypairs.derive_keypair(candidate_seed, algorithm=algo)
            priv_key, pub_key = kp

            # DEBUG: show candidate
            print(f"Trying {candidate_seed} ({algo}) => {pub_key}")

            if pub_key != KNOWN_PUBLIC_KEY:
                continue

            addr = addresscodec.classic_address(pub_key)
            if addr == KNOWN_ADDRESS:
                print("\nFOUND MATCHING SEED!")
                print("Seed:", candidate_seed)
                print("Algorithm:", algo)
                print("Public key:", pub_key)
                print("Address:", addr)
                exit(0)

        except Exception as e:
            print(f"Skipping {candidate_seed} ({algo}): {e}")

print("\n[!] No matching seed found. Double-check:")
print("    - '?' 위치가 정확한지")
print("    - KNOWN_PUBLIC_KEY 포맷이 derive_keypair()와 맞는지")
print("    - Seed가 정말 하나만 미확인 문자인지")
