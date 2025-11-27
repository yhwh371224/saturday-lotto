import xrpl
from xrpl.core import addresscodec


SEED_TEMPLATE = "sEdXXXXXXXXXXXXXXXXXXXXXX?XXX"
UNKNOWN_POS = 27

KNOWN_PUBLIC_KEY = "EDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
KNOWN_ADDRESS = "rXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

CANDIDATES = ["m", "n"]
ALGORITHMS = ["ed25519", "secp256k1"]

for c in CANDIDATES:
    seed_list = list(SEED_TEMPLATE)
    seed_list[UNKNOWN_POS - 1] = c
    candidate_seed = "".join(seed_list)

    for algo in ALGORITHMS:
        try:
            priv_key, pub_key = xrpl.core.keypairs.derive_keypair(candidate_seed, algorithm=algo)

            if pub_key == KNOWN_PUBLIC_KEY:
                addr = addresscodec.classic_address(pub_key)
                if addr == KNOWN_ADDRESS:
                    print(f"FOUND MATCHING SEED: {candidate_seed}")
                    print(f"Algorithm: {algo}")
                    print(f"Address: {addr}")
                    exit(0)

        except Exception as e:
            print(f"Skipping {candidate_seed} ({algo}): {e}")

print("No matching seed found. Check '?' position or key info.")
