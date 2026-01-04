from xrpl.wallet import Wallet

# ---------------------------------------
# USER INPUT
# ---------------------------------------
SEED = "Please input seed here !"

# ---------------------------------------
# Seed → Keypair
# ---------------------------------------
try:
    wallet = Wallet.from_seed(SEED)

    print("=== XRPL Key Info ===")
    print(f"Seed:          {SEED}")
    print(f"Private Key:   {wallet.private_key}")
    print(f"Public Key:    {wallet.public_key}")
    print(f"Classic Addr:  {wallet.classic_address}")

except Exception as e:
    print(f" Failed to derive wallet from seed: {e}")
