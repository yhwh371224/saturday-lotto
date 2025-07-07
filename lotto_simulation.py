import random

# 45개의 번호중 22개의 번호를 선택하고 
# 22개의 번호중에 6개 번호를 선택하여 당첨될 확률 계산이다

def lotto_simulation(drawn_numbers, tries, target_numbers):
    num_matches = 0
    for _ in range(tries):
        draw = random.sample(drawn_numbers, 6)  # 무작위로 6개의 번호 선택
        if all(number in draw for number in target_numbers):
            num_matches += 1
    probability = num_matches / tries
    return probability

# 1에서 45까지의 번호 중 22개를 선택
numbers = list(range(1, 46))
random.shuffle(numbers)
drawn_numbers = random.sample(numbers, 22)


total = []
# 로또 당첨 번호
for i in range(int(10)):
    winner_numbers = random.sample(drawn_numbers, 6)
    winner_numbers.sort()
    total.append(winner_numbers)

for numbers in total:
    print(numbers)


# 시뮬레이션을 통해 확률 계산
tries = 1000000  # 시뮬레이션 시도 횟수
probability = lotto_simulation(drawn_numbers, tries, numbers)

print("확률:", probability)






