'''
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''
# https://drive.google.com/file/d/1_mbieM2ZTR-o5vL5gAid4V2Jq5DkzdS2/view?usp=sharing


n = int(input('Введите количество элементов последовательности: '))
a = 1
summ = a
for i in range(n-1):
    a = a / 2
    if i % 2 == 0:
        summ -= a
    else:
        summ += a

print(f'Сумма эллементов: {summ}')
