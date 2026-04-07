def calc_sin(x, eps):
    term = x
    s = x
    n = 1

    while abs(term) >= eps:
        # Рекурентна формула: наступний член ряду через попередній
        term = -term * x ** 2 / (2 * n * (2 * n + 1))
        s += term
        n += 1

    return s, n