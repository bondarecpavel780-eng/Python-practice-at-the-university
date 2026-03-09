def f1(x, y):
    z = x + y
    x += 1
    y -= 1
    tmp = f2(z, x, y)
    print(x, y, z)
    return tmp

def f2(x, y, z):
    tmp = x + y + z
    x = y = z = 0
    return tmp

x = 0
y = 1
z = 2
res = f1(y, x)
print(x, y, z, res)