from collections import defaultdict

a = defaultdict()
print(a)

s = 'qwweerrttyyuuuiioop'
data = defaultdict(int)
for char in s:
    data[char] += 1

print(data)

print(int())

def my_func():
    return False

new_data = defaultdict(my_func)
new_data[1] = 'hello'
print(new_data[1])
print(new_data[2])
