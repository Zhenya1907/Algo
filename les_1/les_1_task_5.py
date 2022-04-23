'''
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''

# https://drive.google.com/file/d/1txu0kFXzWnqCf5EyZpEldjylUkY73KKQ/view?usp=sharing

a = input('Укажите первую букву: ')
b = input('Укажите вторую букву: ')
pos_a = ord(a) - 96
pos_b = ord(b) - 96
dist = (pos_b - pos_a) - 1
print(
    f'Позиция буквы {a}: {pos_a}\nПозиция буквы {b}: {pos_b}\nКоличество символов между буквами: {dist}')
