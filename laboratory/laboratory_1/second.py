
number_str = "10101"

bases = [2, 8, 16]

print(f"Переклад числа {number_str} у десяткову систему:")
for p in bases:
    result = int(number_str, p)
    print(f"Основа P = {p:2}: результат = {result}")