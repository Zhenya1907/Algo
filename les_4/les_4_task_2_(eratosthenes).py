from math import ceil, log
import timeit

def eratos_sieve(pos):

    base_length = ceil(2 * pos * log(pos)) + 2
    base_list = [i for i in range(base_length+1)]
    base_list[1] = 0

    i = 2
    while i < base_length:
        if base_list[i] != 0:
            new = i * 2
            while new < base_length:
                base_list[new] = 0
                new = new + i
        i = i + 1

    prime_list = []
    for item in base_list:
        if item != 0:
            prime_list.append(item)

    return prime_list[pos-1]

pos = pos = int(input('Укажите позицию простого числа: '))
print(f'На позиции {pos} находится простое число {eratos_sieve(pos)}')

print(timeit.timeit('eratos_sieve(100)', number=1000, globals=globals())) #  0.46932019999999985
print(timeit.timeit('eratos_sieve(1000)', number=1000, globals=globals())) # 7.636534300000001
print(timeit.timeit('eratos_sieve(10000)', number=1000, globals=globals())) # 139.1809269
print(timeit.timeit('eratos_sieve(100000)', number=1000, globals=globals())) # 2219.2243488999998