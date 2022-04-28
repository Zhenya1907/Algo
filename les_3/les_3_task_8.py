SIZE_M = 5
SIZE_L = 3
matrix = [[int(input('Число: ')) for _ in range(SIZE_L)]
          for _ in range(SIZE_M)]
print(*matrix, sep='\n')


STEP = 5
for line in matrix:
    sum_line = 0
    for item in line:
        sum_line += item
        print(f'{item:>{STEP}}', end='')
    print(f'{sum_line:>{STEP * 2}}')
