def f1(x, y, z):
    x -= 1
    y += 1
    z += 2
    print(x, y, z)
    tmp = f2(x, y, z)
    print(x, y, z)
    return tmp

def f2(x, y, z):
    x, y, z = x, z, y
    print(x, y, z)
    return x + y + z

x = 0
y = 1
z = 2
res = f1(x, y, z)
print(x, y, z, res)