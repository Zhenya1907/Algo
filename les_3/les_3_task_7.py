from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


count = 0
while count < 2:
    min_ = array[0]
    for item in array:
        if item < min_:
            min_ = item
    print(f'Минимальный элемент массива: {min_}')
    array.remove(min_)
    count += 1
