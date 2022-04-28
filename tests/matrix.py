from random import randint

SIZE_M = 4
SIZE_N = 6
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)]
          for _ in range(SIZE_M)]
print(*matrix, sep='\n')


STEP = 5
sum_column = [0] * len(matrix[0])
print(sum_column)

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item
        
        print(f'{item:>{STEP}}', end='')
    print(f'{sum_line:>{STEP * 2}}')

for item in sum_column:
    print(f'{item:>{STEP}}', end='')
