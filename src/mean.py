import numpy as np

from decorators import profile
from utils import build_test_list


@profile
def loop_mean(list):
    total = 0
    count = 0
    for entry in list:
        total += entry
        count += 1

    return total / count


@profile
def mean(list):
    return float(sum(list)) / len(list)


@profile
def numpy_mean(np_arr):
    return np.mean(np_arr)


def main():
    for length in [10**x for x in range(4, 8)]:
        list = build_test_list(length)
        np_arr = np.array(list)

        result = loop_mean(list)
        print(f"loop_mean@{length}: {result}")

        result = mean(list)
        print(f"mean@{length}: {result}")

        result = numpy_mean(np_arr)
        print(f"numpy_mean@{length}: {result}")


if __name__ == "__main__":
    main()
