from collections import defaultdict


num = int(input('Количество компаний: '))
d = defaultdict(list)
for _ in range(num):
    company = input('Наименование компании: ')
    money = list(map(float, input('Прибыль за 4 квартала через пробел: ').split(' ')))
    average = sum(money)/len(money)
    d[company].append(money)
    d[company].append(average)
        
general_average = 0
for company in d:
    general_average += d[company][1]
general_average = general_average/len(d)

for company in d:
    if d[company][1] >= general_average:
        d[company].append(True)
    if d[company][1] < general_average:
        d[company].append(False)


print('\nКомпании с прибылью выше среднего: ')
for company in d:
    if d[company][2] == True:
        print(company)

print('\nКомпании с прибылью ниже среднего: ')
for company in d:
    if d[company][2] == False:
        print(company)


