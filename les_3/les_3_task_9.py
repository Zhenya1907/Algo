from random import randint

SIZE_M = 4
SIZE_L = 6
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_L)]
          for _ in range(SIZE_M)]
print(*matrix, sep='\n')


min_list = matrix[0]
for line in matrix:
    for i, item in enumerate(line):
        if item < min_list[i]:
            min_list[i] = item
print(f'Минимальные эллементы столбцов матрицы: {min_list}')

max_item = min_list[0]
for item in min_list:
    if item > max_item:
        max_item = item
print(f'Максимальное число из минимальных в столбцах: {max_item}')
