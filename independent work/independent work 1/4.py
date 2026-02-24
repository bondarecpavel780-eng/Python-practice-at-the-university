print("Введіть 3 цілих числа і число n")
n = int(input("n: "))
count = 3

arr = []
for i in range(count):
    x = int(input(f"Число {i+1}: "))
    if x < n:
        arr.insert(i, x)

print(arr)




