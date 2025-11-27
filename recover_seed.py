#!/usr/bin/env python3
import xrpl
from xrpl.core import addresscodec

# ---------------------------------------
# USER INPUT
# ---------------------------------------
SEED_M = "여기에_m_버전_seed를_넣으세요"
SEED_N = "여기에_n_버전_seed를_넣으세요"

KNOWN_PUBLIC_KEY = "EDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
KNOWN_ADDRESS = "rXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# 두 후보만 검사
CANDIDATES = [SEED_M, SEED_N]
ALGORITHMS = ["ed25519", "secp256k1"]

print("[+] Checking which seed is correct...\n")

for candidate_seed in CANDIDATES:
    print(f"[*] Testing seed → {candidate_seed}")

    for algo in ALGORITHMS:
        try:
            priv, pub = xrpl.core.keypairs.derive_keypair(candidate_seed, algorithm=algo)
            addr = addresscodec.classic_address(pub)

            print(f"    - Derived pub ({algo}): {pub}")
            print(f"    - Derived addr: {addr}")

            if pub == KNOWN_PUBLIC_KEY and addr == KNOWN_ADDRESS:
                print("\n✅ FOUND MATCHING SEED!")
                print(f"Seed:      {candidate_seed}")
                print(f"Algorithm: {algo}")
                print(f"Public Key:{pub}")
                print(f"Address:   {addr}\n")
                exit(0)

        except Exception as e:
            print(f"    - Invalid for {algo}: {e}")

print("\n❌ No matching seed found. Check your seed or known public key/address.")
