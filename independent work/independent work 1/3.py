import math

x = float(input("x: "))
if x >= 0:
    f = 0.5 - math.pow(abs(x), 1/4)
else:
    if abs(x + 1) == 0:
        print("Помилка")

    f = (math.sin(x**2))**2 / abs(x + 1)

print("f(x) =", f)
