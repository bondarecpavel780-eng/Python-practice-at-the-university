import math

def get_valid_input():
    while True:
        try:
            x = float(input("x: "))
            eps = float(input("eps (>0): "))
            if eps > 0:
                return x, eps
        except ValueError:
            pass

def print_result(x, result, iters):
    print(f"sin(x) taylor: {result}")
    print(f"sin(x) math:   {math.sin(x)}")
    print(f"Iterations:    {iters}")