import time
import matplotlib.pyplot as plt
from math_core import taylor_sin

RUNS = 10000
MAX_EPS_POWER = 16
TEST_X_VALUES = [0.5, 3.14, 15.0]


def plot_performance():
    eps_list = [10 ** -i for i in range(1, MAX_EPS_POWER)]

    for x in TEST_X_VALUES:
        iters_list = []
        times_list = []

        for eps in eps_list:
            start = time.perf_counter()
            for _ in range(RUNS):
                _, iters = taylor_sin(x, eps)
            times_list.append(time.perf_counter() - start)
            iters_list.append(iters)

        plt.plot(iters_list, times_list, marker='o', label=f"x = {x}")

    plt.xlabel("Iterations")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()