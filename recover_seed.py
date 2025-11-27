#!/usr/bin/env python3
import xrpl
from xrpl.core import addresscodec

# ---------------------------------------
# USER INPUT
# ---------------------------------------
SEED_M = "sEdXXXXXXXXXXXXXXXXXXXXXXmXXX"  # m 버전
SEED_N = "sEdXXXXXXXXXXXXXXXXXXXXXXnXXX"  # n 버전

KNOWN_PUBLIC_KEY = "EDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
KNOWN_ADDRESS = "rXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

CANDIDATES = [("m", SEED_M), ("n", SEED_N)]
ALGORITHMS = ["ed25519", "secp256k1"]

print("[+] Trying m / n seeds...\n")

for label, candidate_seed in CANDIDATES:
    print(f"[*] Testing seed with '{label}' → {candidate_seed}")

    for algo in ALGORITHMS:
        try:
            priv, pub = xrpl.core.keypairs.derive_keypair(candidate_seed, algorithm=algo)
            print(f"    - Derived pub ({algo}): {pub}")

            if pub == KNOWN_PUBLIC_KEY:
                addr = addresscodec.classic_address(pub)
                if addr == KNOWN_ADDRESS:
                    print("\n====================================")
                    print("  FOUND MATCHING SEED!")
                    print("====================================")
                    print("Seed:      ", candidate_seed)
                    print("Algorithm: ", algo)
                    print("Public Key:", pub)
                    print("Address:   ", addr)
                    print("====================================\n")
                    exit(0)

        except Exception as e:
            print(f"    - Invalid for {algo}: {e}")

print("\n[!] No matching seed found.")
print("    → m/n 둘 다 틀렸거나")
print("    → 공개키/주소 포맷이 실제 derive_keypair 출력과 다르거나")
print("    → 실제 seed가 Ed25519인지 Secp256인지 다를 수 있음")
