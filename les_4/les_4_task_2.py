from math import ceil, log
import timeit

def prime_numbers_pos(pos):
    list_prime = [2]
    end = ceil(2*pos * log(pos)) + 2
    root = int(end**0.5) + 2

    for i in range(3, end, 2):
        f = True
        for item in list_prime:
            if item > root:
                break
            if i % item == 0:
                f = False
                break
        if f:
            list_prime.append(i)

    return list_prime[pos-1]

print(prime_numbers_pos(10))


pos = int(input('Укажите позицию простого числа: '))
print(f'На позиции {pos} находится простое число {prime_numbers_pos(pos)}')

print(timeit.timeit('prime_numbers_pos(100)', number=1000, globals=globals())) # 0.3169561000000005
print(timeit.timeit('prime_numbers_pos(1000)', number=1000, globals=globals())) # 7.5846385000000005
print(timeit.timeit('prime_numbers_pos(10000)', number=1000, globals=globals())) # 193.7275465
print(timeit.timeit('prime_numbers_pos(100000)', number=1000, globals=globals())) # 5591.442762


