from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = 555
pos = 2
# array.insert(pos, num)

# insert 1 (spend time)
array.append(None)
i = len(array) - 1
while i > pos:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1
    print(array)

# insert 2 (spend time and memory)
array = array[:pos] + [num] + array[pos:]
print(array)
