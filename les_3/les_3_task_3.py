from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Основной массив: {array}')


min_ = array[0]
max_ = array[0]
pos_min = 0
pos_max = 0
for i, item in enumerate(array):
    if item < min_:
        min_ = item
        pos_min = i
    if item > max_:
        max_ = item
        pos_max = i

array[pos_min], array[pos_max] = array[pos_max], array[pos_min]
print(f'Измененный массив: {array}')
