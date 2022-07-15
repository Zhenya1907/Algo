from collections import Counter

a = Counter()
b = Counter('adsfdgdrdfdddfdff')
c = Counter({'cat': 10, 'dog': 5})

print(a, b, c, sep='\n')

print(b['z'])

b['z'] = 6
print(b)

print(b.most_common(3))

x = Counter(a=2, b=-1, c=5)
y = Counter(a=1, b=3, c=-4)
print(x,y, sep='\n')
print(x + Counter())
print(x + y)
print(x - y)
print(x & y)
print(x | y)


















