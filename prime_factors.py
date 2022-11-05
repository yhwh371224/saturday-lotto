
prime_factors = []
divisor = 2
x = 600851475143
while divisor <= x:
    if x % divisor == 0:
        prime_factors.append(divisor)
        x = x/divisor
    else:
        divisor += 1
print(prime_factors)
print(prime_factors.pop())
