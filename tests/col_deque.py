from collections import deque

a = deque()
b = deque('abrakadabra', maxlen=5)
c = deque([1, 2 , 3, 4])


print(a, b, c, sep='\n')

d = deque((1, 2, 3))
print(d)
d.append(4)
print(d)
d.appendleft(5)
print(d)
d.extend([6, 7])
print(d)
d.extendleft([8, 9])
print(d)
spam = d.pop()
spaml = d.popleft()
print(spam, spaml, d)
print(d[3])
d.rotate(3)
print(d)