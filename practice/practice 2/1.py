numbers = list(map(float, input().split()))
numbers.sort()
n = len(numbers)

if n % 2 == 1:
    print(numbers[n // 2])
else:
    print((numbers[n // 2 - 1] + numbers[n // 2]) / 2)