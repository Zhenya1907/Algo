from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array.sort()
print(array)


find = int(input('Какое число найти: '))
len_ = len(array)
pos = len_ // 2
left = 0
right = len_ - 1

while find != array[pos] and left <= right:
    if find > array[pos]:
        left = pos + 1
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print(f'Эллемент отсутствует' if left > right else f'Эллемент в позиции {pos}')
