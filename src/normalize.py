import math
import numpy as np

from decorators import profile
from utils import build_test_list


@profile
def loop_norm(list):
    list_max = -math.inf
    list_min = math.inf
    for entry in list:
        if entry < list_min:
            list_min = entry
        if entry > list_max:
            list_max = entry

    result = []
    for entry in list:
        result.append((entry - list_min) / (list_max - list_min))

    return result


@profile
def norm(list):
    list_max = max(list)
    list_min = min(list)
    return [(entry - list_min) / (list_max - list_min) for entry in list]


@profile
def numpy_norm(np_arr):
    return (np_arr - np.min(np_arr)) / (np.max(np_arr) - np.min(np_arr))


def main():
    for length in [10**x for x in range(4, 8)]:
        list = build_test_list(length)
        np_arr = np.array(list)

        result = loop_norm(list)
        print(f"loop_norm@{length} check: {result[:5]}")

        result = norm(list)
        print(f"norm@{length} check: {result[:5]}")

        result = numpy_norm(np_arr)
        print(f"numpy_norm@{length} check: {result[:5]}")


if __name__ == "__main__":
    main()
