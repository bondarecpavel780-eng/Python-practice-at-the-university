import math
def coordinates():
    print("\n Ввід координат ")
    mode = input("Виберіть 2D або 3D: ").lower()

    if mode == "2d":
        x = float(input("x = "))
        y = float(input("y = "))
        print(f"Точка: ({x}, {y})")

    elif mode == "3d":
        x = float(input("x = "))
        y = float(input("y = "))
        z = float(input("z = "))
        print(f"Точка: ({x}, {y}, {z})")

    else:
        print("Невірний вибір")

def math_expressions():
    print("\n Обчислення виразів")
    a = float(input("a = "))
    b = float(input("b = "))

    try:
        expr1 = math.log(a**2 + b**2)
        expr2 = math.sin((a + b)**(1/7))
        expr3 = math.cos(a**12 + b**12)**3

        print(f"ln(a²+b²) = {expr1:.5f}")
        print(f"sin((a+b)^(1/7)) = {expr2:.5f}")
        print(f"cos³(a¹²+b¹²) = {expr3:.5f}")
    except:
        print("Помилка")

def triangle_perimeter():
    print("\n Периметр трикутника")
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))

    if a + b > c and a + c > b and b + c > a:
        p = a + b + c
        print(f"Периметр P = {p}")
    else:
        print("Помилка")

def math_functions():
    print("\n Функції math ")
    x = float(input("Введіть число: "))

    print("sqrt =", math.sqrt(x))
    print("log =", math.log(x))
    print("sin =", math.sin(x))
    print("cos =", math.cos(x))
    print("tan =", math.tan(x))
    print("factorial =", math.factorial(int(x)))
    print("exp =", math.exp(x))

def circle():
    print("\n Робота з колом ")
    l = float(input("Довжина кола L = "))

    r = l / (2 * math.pi)
    s = math.pi * r**2

    print(f"Радіус r = {r:.4f}")
    print(f"Площа S = {s:.4f}")

def formatting():
    print("\n Форматування чисел ")
    num = float(input("Число: "))
    n = int(input("Кількість знаків після коми: "))

    print("Fixed-point:", f"{num:.{n}f}")
    print("Scientific:", f"{num:.{n}e}")

def linear_equation():
    print("\n Рівняння ax + b = 0 ")
    a = float(input("a = "))
    b = float(input("b = "))

    if a == 0:
        print("0 розв'язків")
    else:
        x = -b / a
        print(f"x = {x:.4f}")

def greet():
    print("\n Привітання ")
    name = input("Ім'я: ")
    surname = input("Прізвище: ")
    print(f"Вітаю, {name} {surname}")

def menu():
    while True:
        print("""
========= МЕНЮ =========
1. Координати (2D/3D)
2. Математичні вирази
3. Периметр трикутника
4. Функції math
5. Робота з колом
6. Форматування чисел
7. Рівняння ax + b = 0
8. Привітання
0. Вихід
========================
""")

        choice = input("Оберіть пункт: ")

        if choice == "1":
            coordinates()
        elif choice == "2":
            math_expressions()
        elif choice == "3":
            triangle_perimeter()
        elif choice == "4":
            math_functions()
        elif choice == "5":
            circle()
        elif choice == "6":
            formatting()
        elif choice == "7":
            linear_equation()
        elif choice == "8":
            greet()
        elif choice == "0":
            print("до побачення")
            break
        else:
            print("невірний вибір")

menu()