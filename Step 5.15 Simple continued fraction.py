# x, y = map(int, input().split('/'))
# print(x, y)
m, n = 239, 30

fractions = []
a = int(x/y)
x = x - y * a
while int(y/x) != 0:
    print('a', a)
    print('x', x)
    print('y', y)
    fractions.append(a)
    a = int(y/x)
    y = y - a * x

print(fractions)

