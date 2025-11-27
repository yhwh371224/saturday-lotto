#!/usr/bin/env python3
from xrpl.core.keypairs import derive_keypair, derive_classic_address

# ---------------------------------------
# USER INPUT
# ---------------------------------------
SEED = "여기에_your_seed를_넣으세요"

# ---------------------------------------
# Seed → Keypair
# ---------------------------------------
try:
    # Ed25519 기준
    priv_key, pub_key = derive_keypair(SEED, algorithm="ed25519")
    classic_addr = derive_classic_address(pub_key)

    print("=== XRPL Key Info ===")
    print("Seed (입력):", SEED)
    print("Private Key:", priv_key)
    print("Public Key: ", pub_key)
    print("Classic Address:", classic_addr)

except Exception as e:
    print("Error deriving keypair:", e)
