import time
import random

random.seed(time.time())

print("✅ How many total numbers you like to choose?")
c = input()
print('')

# 28 numbers
# 7pDg t2Nz TL1r 2Z6g 6gv4 vPYs 3Lmm 
numbers = list(range(1, 46))
numbers_picked = random.sample(numbers, int(c))
print(numbers_picked)
print('')

print('✅ How many games would you like to play?')
n = input()
print('')

print('✅ Please find your numbers below, Good luck!')
print('')

for i in range(int(n)):
    winner_numbers = random.sample(numbers_picked, 6)
    winner_numbers.sort()
    print('')
    print(f"💰 {i+1}회: {winner_numbers}")
    print('')
