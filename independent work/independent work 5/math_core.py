import math

def taylor_sin(x, eps):
    x = (x + math.pi) % (2 * math.pi) - math.pi
    term = x
    sin_val = x
    n = 1

    while abs(term) >= eps:
        term *= -(x * x) / ((2 * n) * (2 * n + 1))
        sin_val += term
        n += 1

    return sin_val, n