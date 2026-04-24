import io_mod
import calc_mod
import perf_mod

# 1. Ввід даних
x = io_mod.get_number("Введіть x: ")
eps = io_mod.get_eps()

# 2. Обчислення
sin_x, iters = calc_mod.calc_sin(x, eps)

# 3. Вивід
io_mod.print_result(x, sin_x, iters)

# 4. Аналіз продуктивності (графік)
print("\nБудуємо графік продуктивності...")
perf_mod.run_analysis()