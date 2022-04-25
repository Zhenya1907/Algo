'''
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
'''
# https://drive.google.com/file/d/1E7axXoN4rDhZy2R2og8K0z4647Bn_3qb/view?usp=sharing


def summ(n):
    if n == 1:
        return n
    if n > 1:
        return summ(n - 1) + n


num = int(input('Введите натуральное число: '))
a = summ(num)
b = num * (num + 1) / 2
if a == b:
    print('Равенство выполняется')
else:
    print('Равенство не выполняется')
