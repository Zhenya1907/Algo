import timeit
import cProfile

N = 1_000
a = [i for i in range(N)]

print(timeit.timeit('a = [i for i in range(100)]', number=100, globals=globals()))
print(timeit.timeit('a = [i for i in range(1000)]', number=100, globals=globals()))
print(timeit.timeit('a = [i for i in range(10000)]', number=100, globals=globals()))
print(timeit.timeit('a = [i for i in range(100000)]', number=100, globals=globals()))
print(timeit.timeit('a = [i for i in range(1000000)]', number=100, globals=globals()))


def get_len(data):
    return len(data)


def get_sum(data):
    sum_ = 0
    for item in data:
        sum_ += item
    return sum_


def main(n):
    my_list = [i for i in range(n)]
    len_test = get_len(my_list)
    sum_test = get_sum(my_list)
    len_ = get_len(my_list)
    sum_ = sum(my_list)
    return sum_, len_


cProfile.run('main(10_000_000)')
