def get_number(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Помилка! Введіть число.")

def get_eps():
    while True:
        eps = get_number("Введіть точність eps (>0): ")
        if eps > 0:
            return eps
        print("Помилка! Точність має бути більшою за 0.")

def print_result(x, sin_x, iters):
    print(f"sin({x}) = {sin_x}")
    print(f"Кількість ітерацій: {iters}")