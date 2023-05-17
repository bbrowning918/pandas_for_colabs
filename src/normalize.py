import numpy as np

from decorators import profile
from utils import build_test_arr

@profile
def normalize(arr):
    arr_max = max(arr)
    arr_min = min(arr)
    return [(i - arr_min) / (arr_max - arr_min) for i in arr] 

@profile
def numpy_normalize(np_arr):
    return (np_arr - np.min(np_arr)) / (np.max(np_arr) - np.min(np_arr))

def main():
    for l in [10 ** x for x in range(4, 8)]:
        arr = build_test_arr(l)
        np_arr = np.array(arr)

        result = normalize(arr)
        print(F"normalize@{l} check: {result[:5]}")

        result = numpy_normalize(np_arr)
        print(F"numpy_normalize@{l} check: {result[:5]}")

if __name__ == "__main__":
    main()

