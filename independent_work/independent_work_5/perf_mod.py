import time
import matplotlib.pyplot as plt
import calc_mod


def run_analysis():
    iters_list = []
    times_list = []

    # Різні значення x для емпіричного аналізу
    test_values = [1, 5, 10, 15, 20, 25, 30, 40]
    eps = 0.0001

    for x in test_values:
        start_time = time.time()
        _, iters = calc_mod.calc_sin(x, eps)
        end_time = time.time()

        iters_list.append(iters)
        times_list.append(end_time - start_time)

    # Побудова графіка
    plt.plot(iters_list, times_list, marker='o')
    plt.xlabel('Кількість ітерацій')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Залежність часу від кількості ітерацій')
    plt.grid()
    plt.show()