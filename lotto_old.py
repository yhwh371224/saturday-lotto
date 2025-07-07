from random import *

print('How many games would you like to pick?')

n = input()

print('Please find your random numbers in',
      n, 'games as you picked. Good luck!')


lotto_number = list(range(1, 46))
shuffle(lotto_number)

total = []
for i in range(int(n)):
    shuffle(lotto_number)
    winner_numbers = sample(lotto_number, 6)
    winner_numbers.sort()
    print('Saturday Lotto numbers')
    print(winner_numbers)
    print('*'*25)
    total.append(winner_numbers)

re_total = [single_nums for each_row in total for single_nums in each_row]

print("뽑힌 번호들 모두 모으면:")
print(re_total)

final_re_total = list(dict.fromkeys(re_total))

print()
print("위에서 중복된 번호를 제외하면:")
print(final_re_total)

final_num = sample(final_re_total, 6)

print()
print("위 번호에서 6개 번호만 랜덤하게 뽑으면")
print(final_num)

lest_numbers = [i for i in lotto_number if not i in final_re_total]

print()
print("남겨진 번호들만 모으면:")
print(lest_numbers)
print()
print("이 중에 다시 6개 번호만 뽑으면")

print(sample(lest_numbers, 6))
