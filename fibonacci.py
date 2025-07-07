def fib(n):
    if 0 <= n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


total = [fib(i) for i in range(2, 34)]
even_numbers = [i for i in total if i % 2 == 0]
print('Answer = ', sum(even_numbers))


fib = [1, 2, 3]
sumFE = 0
while fib[0] < 4e6:
    if fib[0] % 2 == 0:
        sumFE += fib[0]
    fib.append(sum(fib[1:]))
    del fib[0]
print('Answer = ', sumFE)


# first = 1
# second = 2
# sum = 0
# while first < 4e6:
#    new = first + second
#    first = second
#    second = new
#    if first % 2 == 0:
#        sum = sum + first
# print(sum)
