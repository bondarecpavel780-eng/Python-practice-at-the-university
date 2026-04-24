count = 3
arr = []
print("Введіть 3 числа: ")
for i in range(count):
    x = int(input(f"Число {i +1}: "))
    arr.insert(i, x)
print(arr)

print(min(arr))
print(max(arr))