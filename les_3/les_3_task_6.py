from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


min_ = array[0]
max_ = array[0]
pos_min = 0
pos_max = 0
sum_ = 0
for i, item in enumerate(array):
    if item < min_:
        min_ = item
        pos_min = i
    if item > max_:
        max_ = item
        pos_max = i

if pos_min < pos_max:
    array = array[pos_min + 1: pos_max]
if pos_min > pos_max:
    array = array[pos_max + 1: pos_min]

for item in array:
    sum_ += item

print(f'Новый массив: {array}\nСумма эллементов: {sum_}')
