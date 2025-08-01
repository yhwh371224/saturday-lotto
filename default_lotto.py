import time
import random
from root_input import *


random.seed(time.time())

lotto_number = list(range(int(min), int(max)))
random.shuffle(lotto_number)

for i in range(int(n)):
    winner_numbers = random.sample(lotto_number, int(z))
    winner_numbers.sort()
    print('')
    print(f"✨ {i+1}회: {winner_numbers}")
    print('')


