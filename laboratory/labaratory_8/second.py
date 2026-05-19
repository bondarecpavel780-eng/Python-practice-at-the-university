def return_none_on_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return None
    return wrapper

# Приклад використання:
@return_none_on_exception
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))  