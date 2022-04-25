'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.
'''
# https://drive.google.com/file/d/1p-_3t5VWXeYB1HHdJBXPqyJLtRYBC5cV/view?usp=sharing


n = int(input('Введите число: '))
revers = ''
while n > 9:
    revers += str(n % 10)
    n = n // 10

revers += str(n)
print(int(revers))
