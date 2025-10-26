import os
import string
import random
from datetime import datetime

secure_folder = os.path.expanduser('~/.secure')
os.makedirs(secure_folder, exist_ok=True)

today = datetime.now().strftime('%Y-%m-%d')

names = [
    "info@",
    "sungkam3@",
    "junghee@",
    "commbank",
    "anz (nab)",
    "westpac",
    "coinspot",
    "paypal",
    "stripe",
    "ozlotto",
    "github",
    "bitwarden",
    "vultr",
    "crazy",
    "cloudfare",
]

if len(names) != 15:
    print("⚠️  Please double check if there are 15 names.")
    exit()

def generate_password(length=24):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

password_lines = []
password_lines.append(f"Generated on: {today}")
password_lines.append('-' * 40)
for name in names:
    password = generate_password()
    password_lines.append(f"{name.ljust(15)} :  {password}")

# 저장 파일 경로에 날짜 포함
plain_file = os.path.join(secure_folder, f'password_{today}.txt')

# 파일 작성
with open(plain_file, 'w') as f:
    f.write('\n'.join(password_lines) + '\n')
    f.write('\n' + '=' * 40 + '\n\n')  # 시각적 구분선
    f.write('\n'.join(password_lines) + '\n')

# 보안 권한 설정
os.chmod(secure_folder, 0o700)
os.chmod(plain_file, 0o600)

print(f'✅  15 passwords created twice in {plain_file}.\n')

# 화면에 4번 출력: 좌측 상단, 우측 상단, 좌측 하단, 우측 하단 느낌으로
block = '\n'.join(password_lines)
separator = ' ' * 10  # 좌우 여백

print(block + separator + block)
print('\n' * 2)
print(block + separator + block)
