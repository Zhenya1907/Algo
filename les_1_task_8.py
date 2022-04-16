'''
8. Определить, является ли год, который ввел пользователь, високосным или не високосным.
'''

# https://drive.google.com/file/d/184YhA7EKFOEFRAvFmubINBDnYo2j_yJT/view?usp=sharing

print('Введите год: ')
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Год вискокосный')
        else:
            print('Год не високосный')
    else:
        print('Год високосный')
else:
    print('Год не високосный')
