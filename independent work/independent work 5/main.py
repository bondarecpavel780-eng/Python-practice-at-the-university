from io_utils import get_valid_input, print_result
from math_core import taylor_sin
from performance import plot_performance

def main():
    x, eps = get_valid_input()
    result, iters = taylor_sin(x, eps)
    print_result(x, result, iters)
    plot_performance()

if __name__ == "__main__":
    main()