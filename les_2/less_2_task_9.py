'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
'''
# ссылка


def digits_sum(n):
    count = 0
    if n < 10:
        return count + n
    if n >= 10:
        count = count + n % 10
        return count + digits_sum(n // 10)


num = int(input('Введите натуральное число (для выхода - 0): '))
max_sum = 0
search_num = 0
while num != 0:
    res = digits_sum(num)
    if max_sum < res:
        max_sum = res
        search_num = num
    num = int(input('Введите натуральное число (для выхода - 0): '))

print(f'Наибольшее число по сумме цифр: {search_num}\nСумма цифр: {max_sum}')
