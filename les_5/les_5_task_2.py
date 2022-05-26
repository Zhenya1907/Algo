from collections import defaultdict, deque


def dec_number(str_):
    num = deque(str_)
    num.reverse()
    dec = 0
    for i in range(len(num)):
        dec += signs_dict[num[i]] * 16 ** i
    return dec


def hex_number(number):
    hex_list = []
    while number > 0:
        a = number % 16
        for key in signs_dict:
            if signs_dict[key] == a:
                hex_list.append(key)
                break
        number = number // 16
    hex_list.reverse()
    s = ''.join(hex_list)
    return s


signs = '0123456789ABCDEF'
signs_dict = defaultdict(int)
count = 0
for key in signs:
    signs_dict[key] = count
    count += 1


n1 = input('Первое шестнадцатиричное число: ').upper()
n2 = input('Второе шестнадцатиричное число: ').upper()

a = dec_number(n1)
b = dec_number(n2)

print(f'Сумма чисел {n1} и {n2}: {hex_number(a + b)}')
print(f'Произведение чисел {n1} и {n2}: {hex_number(a * b)}')