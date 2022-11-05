from random import *
from root_input import *

lotto_number = list(range(int(min), int(max)))
shuffle(lotto_number)

total = []
for i in range(int(n)):
    winner_numbers = sample(lotto_number, int(z))
    winner_numbers.sort()
    print('Random Lotto numbers')
    print(winner_numbers)
    print('*'*25)
    total.append(winner_numbers)

re_total = [single_nums for each_row in total
            for single_nums in each_row]

print()
print('위의 뽑은 번호들을 한데로 모으면;')
re_total.sort()
print(re_total)
print()
print('여기서 중복된 번호를 제외하면;')

re_total = list(set(re_total))

print(re_total)
print()

final_num = sample(re_total, int(z))

print("위에 제외한 번호로 랜덤하게 다시 뽑은 번호는;")
print(final_num)
print()
print("뽑힌 번호는 제외하고 남겨진 번호는;")

rest_nums = [i for i in lotto_number if not i in re_total]

rest_nums.sort()
print(rest_nums)
print()
print(f"그 남겨진 번호에서 다시 {z}개번호만 뽑으면;")

total_rest_nums = sample(rest_nums, int(z))

print(total_rest_nums)
