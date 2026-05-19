def count_arguments(*args):
    return len(args)

print(count_arguments(1, 2, 3, 4, 5, 0, 2, 1, 3, 4))
print(count_arguments("hello", 42))
print(count_arguments())