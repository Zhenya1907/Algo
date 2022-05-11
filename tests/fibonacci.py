import timeit
import cProfile


# 1. Последовательность фибоначчи
def fib(n):
    if n < 2:
        return n
    res = fib(n - 1) + fib(n - 2)
    return res

# 2. Последовательность фибоначчи (рекурсия с технологией меморизации)
def fib(n):
    fib_dict = {0: 0, 1: 1}

    def _fib_func(n):
        if n in fib_dict:
            return fib_dict[n]
        fib_dict[n] = _fib_func(n - 1) + _fib_func(n - 2)
        return fib_dict[n]

    return _fib_func(n)


# 3. Последовательность фибоначчи (циклический алгоритм)
def fib(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for _ in range(n):
        first, second = second, first + second
    return first


def test_fib(func):
    fib_tuple = (0, 1, 1, 2, 3, 5, 8, 13, 21)
    for i, item in enumerate(fib_tuple):
        func(i) == item
        assert func(i) == item, f'Error {i=} {item=}'
        print(f'Test {i} OK')


test_fib(fib)

print(timeit.timeit('fib(2)', number=100, globals=globals()))
print(timeit.timeit('fib(4)', number=100, globals=globals()))
print(timeit.timeit('fib(8)', number=100, globals=globals()))
print(timeit.timeit('fib(16)', number=100, globals=globals()))
print(timeit.timeit('fib(32)', number=100, globals=globals()))
print(timeit.timeit('fib(64)', number=100, globals=globals()))
print(timeit.timeit('fib(128)', number=100, globals=globals()))

cProfile.run('fib(128)')
