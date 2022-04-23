'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

# https://drive.google.com/file/d/1efBmSjjpws1AQDvo9rp1GKo557kkdq1X/view?usp=sharing

print('Введите трехзначное число: ')
n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
summ = a + b + c
mult = a * b * c
print(summ, mult)
