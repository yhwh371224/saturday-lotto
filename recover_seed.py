#!/usr/bin/env python3
import xrpl
from xrpl.core import addresscodec

# -----------------------------
# USER INPUT (세 군데만 수정)
# -----------------------------

# 네가 기억하는 seed (27번째 글자만 '?' 로 표시)
SEED_TEMPLATE = "sEdXXXXXXXXXXXXXXXXXXXXXX?XXX"  # 예시 형태, 너는 직접 수정

# 헷갈리는 위치 (1부터 시작 → 27번째)
UNKNOWN_POS = 27

# 네가 확실히 알고 있는 XRP 주소 (또는 public key)
KNOWN_PUBLIC_KEY = "EDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" 
KNOWN_ADDRESS = "rXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  

# -----------------------------
# Base58 문자 목록
# -----------------------------
BASE58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

correct = []

for c in BASE58:
    # 27번째 글자만 교체
    seed_list = list(SEED_TEMPLATE)
    seed_list[UNKNOWN_POS - 1] = c
    candidate_seed = "".join(seed_list)

    try:
        # Seed → Keypair
        kp = xrpl.core.keypairs.derive_keypair(candidate_seed)
        pub_key = kp[1]
        
        # First check the public key (fast)
        if pub_key != KNOWN_PUBLIC_KEY:
            continue

        # If public key matches, check address too
        addr = addresscodec.classic_address(pub_key)
        if addr == KNOWN_ADDRESS:
            print("\nFOUND MATCHING SEED:", candidate_seed)
            break

    except Exception:
        pass

if not correct:
    print("No matching seed found. Check template or position.")
else:
    print("\nAll matching seeds:")
    for s in correct:
        print(s)


# -----------------------------
# sudo apt install python3-pip
# pip3 install xrpl-py
# -----------------------------


# -----------------------------
# python3 recover_seed.py 
# -----------------------------