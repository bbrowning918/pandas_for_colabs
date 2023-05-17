import numpy as np

from decorators import profile
from utils import build_test_arr

@profile
def loop_mean(arr):
    total = 0
    count = 0
    for entry in arr:
        total += entry
        count += 1

    return total / count

@profile
def mean(arr):
    return float(sum(arr)) / len(arr)

@profile
def numpy_mean(np_arr):
    return np.mean(np_arr)

def main():
    for l in [10 ** x for x in range(4, 8)]:
        arr = build_test_arr(l)
        np_arr = np.array(arr)

        result = loop_mean(arr)
        print(F"loop_mean@{l}: {result}")

        result = mean(arr)
        print(F"mean@{l}: {result}")

        result = numpy_mean(np_arr)
        print(f"numpy_mean@{l}: {result}")

if __name__ == "__main__":
    main()

