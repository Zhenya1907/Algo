'''
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''
# https://drive.google.com/file/d/1OyJ78PGBsZYthyTgIeFqJra6nxwY_0fm/view?usp=sharing


n = int(input('Укажите желаемое количество чисел: '))
digit = input('Введите искомую цифру: ')
counter = 0

for i in range(n):
    number = input('Введите число: ')
    counter += number.count(digit)
print(
    f'Цифра {digit} встречается в указанной последовательности чисел {counter} раз(а)')
