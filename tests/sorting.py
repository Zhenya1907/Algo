import random

# data = [*range(10)]
# print(data)

# random.shuffle(data)
# print(data)

data = [2, 4, 0, 7, 9, 6, 1, 3, 5, 8]

# 1. СОРТИРОВКА ПУЗЫРЬКОМ (O(n**2))
def bubble_sort(data):
    n = 1
    while n < len(data):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
        print(data)

#bubble_sort(data)

# 2. СОРТИРОВКА ВЫБОРОМ (O(n**2))
def selection_sort(array):
    for i in range(len(array)):
        finger = i
        for j in range(i + 1, len(array)):
            if array[j] < array[finger]:
                finger = j
        array[finger], array[i] = array[i], array[finger]

        print(array)

#selection_sort(data)

# 3. СОРТИРОВКА ВСТАВКАМИ (O(n**2))
def insertion_sort(array):
    for i in range(1, len(array)):
        arm = array[i]
        j = i
        while array[j - 1] > arm and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = arm
        print(array)

#insertion_sort(data)

# 4. СОРТИРОВКА СЛИЯНИЕМ + функция для слияния двух массивов
def merge_arrays(left, right):
    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def merge_sort(array):

    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge_arrays(left, right)


print(merge_sort(data))



# 5. СОРТИРОВКА ШЕЛЛА (лучше чем O(n*log(n)) пока данных < 4000, после - замедляется)
def shell_sort(array):
    assert len(array) < 4000, 'Массив больше 4000. Попробуй другую сортировку.'

    def new_inc(array):
        list_inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) < list_inc[-1]:
            list_inc.pop()
        while list_inc:
            yield list_inc.pop()

    for inc in new_inc(array):
        for i in range(inc, len(array)):
            for j in range(i, inc - 1, -inc):
                if array[j - inc] <= array[j]:
                    break
                array[j], array[j - inc] = array[j - inc], array[j]
        print(array)

#shell_sort(data)

# 6. БЫСТРАЯ СОРТИРОВКА (сортировка Хоара), без дополнительных затрат памяти, O(n*log(n)
def quick_sort(array, first, last):

    print(array[first:last + 1])

    if first >= last:
        return

    pivot = array[random.randint(first, last)]
    i = first
    j = last

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    quick_sort(array, first, j)
    quick_sort(array, i, last)


# quick_sort(data, 0, len(data) - 1)
# print(data)

# СОРТИРОВКА "ИЗ КОРОБКИ"
#sorted - сортировка вставками + слияние
from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name={self.name} age={self.age}'

data_ = [Person('Valery', 28),
        Person('Polina', 21),
        Person('Valery', 30),
        Person('Zhenya', 30),
        Person('Liza', 37),
        Person('Liza', 38),
        Person('Julia', 20),
        ]

#print(*data_, sep='\n')

new_data_ = sorted(data_, key=attrgetter('age'))
#print(*new_data_, sep='\n')

the_newest_data_ = sorted(new_data_, key=attrgetter('name'))
print(*the_newest_data_, sep='\n')








