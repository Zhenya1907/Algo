''' Задача 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.'''

# Ссылка на таблицу и вывод:
# https://docs.google.com/spreadsheets/d/1RZ17mXAjQoD7W6xWDenkUyQFg1jsDcmaXyujGWliNI8/edit?usp=sharing


from random import randint
import timeit
import cProfile


def array(size):
    MIN_ITEM = 0
    MAX_ITEM = 100
    arr = [randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    return arr


# Решение 1 (из прошлого дз, удаление элемента, сдвиг всех эллементов, несколько проходов по массиву)
def func_1(size):
    arr = array(size)
    count = 0
    list_min = []
    while count < 2:
        min_ = arr[0]
        for item in arr:
            if item < min_:
                min_ = item
        list_min.append(min_)
        arr.remove(min_)
        count += 1
    return list_min


print(f'Функция 1: {func_1(10)}')

print(timeit.timeit('func_1(100)', number=1000, globals=globals()))  # 0.1406638
print(timeit.timeit('func_1(1000)', number=1000, globals=globals()))  # 1.3101701000000001
print(timeit.timeit('func_1(10000)', number=1000, globals=globals()))  # 13.2548679
print(timeit.timeit('func_1(100000)', number=1000, globals=globals()))  # 144.2097736
print(timeit.timeit('func_1(1000000)', number=1000, globals=globals()))  # 1448.0482551999999

cProfile.run('func_1(1000000)')

'''
Функция 1: [2, 37]
         5266739 function calls in 3.240 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    3.240    3.240 <string>:1(<module>)
        1    0.531    0.531    3.161    3.161 les_4_task_1.py:12(<listcomp>)
        1    0.072    0.072    3.236    3.236 les_4_task_1.py:18(func_1)
        1    0.000    0.000    3.161    3.161 les_4_task_1.py:9(array)
  1000000    0.738    0.000    1.078    0.000 random.py:237(_randbelow_with_getrandbits)
  1000000    0.978    0.000    2.056    0.000 random.py:290(randrange)
  1000000    0.574    0.000    2.630    0.000 random.py:334(randint)
        1    0.000    0.000    3.240    3.240 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
  1000000    0.143    0.000    0.143    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1266729    0.197    0.000    0.197    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.003    0.001    0.003    0.001 {method 'remove' of 'list' objects}
'''


# Решение 2 (сортировка и срез)
def func_2(size):
    arr = array(size)
    arr.sort()
    return arr[:2]


print(f'Функция 2: {func_2(10)}')

print(timeit.timeit('func_2(100)', number=1000, globals=globals()))  # 0.244192599999991
print(timeit.timeit('func_2(1000)', number=1000, globals=globals()))  # 2.23847889999999
print(timeit.timeit('func_2(10000)', number=1000, globals=globals()))  # 19.72311429999999
print(timeit.timeit('func_2(100000)', number=1000, globals=globals()))  # 166.69529160000002
print(timeit.timeit('func_2(1000000)', number=1000, globals=globals()))  # 1468.8166661999999

cProfile.run('func_2(1000000)')

'''
Функция 2: [7, 41]
         5267426 function calls in 3.318 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    3.318    3.318 <string>:1(<module>)
        1    0.508    0.508    3.143    3.143 les_4_task_1.py:12(<listcomp>)
        1    0.000    0.000    3.311    3.311 les_4_task_1.py:45(func_2)
        1    0.000    0.000    3.143    3.143 les_4_task_1.py:9(array)
  1000000    0.744    0.000    1.069    0.000 random.py:237(_randbelow_with_getrandbits)
  1000000    0.986    0.000    2.055    0.000 random.py:290(randrange)
  1000000    0.580    0.000    2.635    0.000 random.py:334(randint)
        1    0.000    0.000    3.318    3.318 {built-in method builtins.exec}
  1000000    0.133    0.000    0.133    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1267419    0.192    0.000    0.192    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.168    0.168    0.168    0.168 {method 'sort' of 'list' objects}
'''


# Решение 3 (один проход по массиву)
def func_3(size):
    arr = array(size)

    if arr[0] < arr[1]:
        min_1, min_2 = arr[0], arr[1]
    else:
        min_1, min_2 = arr[1], arr[0]

    for item in arr[2:]:
        if item < min_1:
            min_2 = min_1
            min_1 = item
        elif item < min_2:
            min_2 = item

    return min_1, min_2


print(f'Функция 3: {func_3(10)}')

print(timeit.timeit('func_3(100)', number=1000, globals=globals()))  # 0.19044009999998934
print(timeit.timeit('func_3(1000)', number=1000, globals=globals()))  # 1.6526706000000218
print(timeit.timeit('func_3(10000)', number=1000, globals=globals()))  # 15.094713599999977
print(timeit.timeit('func_3(100000)', number=1000, globals=globals()))  # 155.0134531
print(timeit.timeit('func_3(1000000)', number=1000, globals=globals()))  # 1356.3361496999996

cProfile.run('func_3(1000000)')

'''
Функция 3: (12, 14)
         5266445 function calls in 3.376 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    3.376    3.376 <string>:1(<module>)
        1    0.525    0.525    3.296    3.296 les_4_task_1.py:12(<listcomp>)
        1    0.074    0.074    3.371    3.371 les_4_task_1.py:67(func_3)
        1    0.000    0.000    3.296    3.296 les_4_task_1.py:9(array)
  1000000    0.810    0.000    1.144    0.000 random.py:237(_randbelow_with_getrandbits)
  1000000    1.008    0.000    2.152    0.000 random.py:290(randrange)
  1000000    0.619    0.000    2.772    0.000 random.py:334(randint)
        1    0.000    0.000    3.376    3.376 {built-in method builtins.exec}
  1000000    0.135    0.000    0.135    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1266439    0.198    0.000    0.198    0.000 {method 'getrandbits' of '_random.Random' objects}
'''
