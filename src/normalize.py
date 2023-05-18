import math
import numpy as np

from decorators import profile
from utils import generate_test_numbers


@profile
def loop_norm(numbers):
    max_number = -math.inf
    min_number = math.inf
    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number

    result = []
    for number in numbers:
        result.append((number - min_number) / (max_number - min_number))

    return result


@profile
def norm(numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    return [(number - min_number) / (max_number - min_number) for number in numbers]


@profile
def numpy_norm(np_array):
    return (np_array - np.min(np_array)) / (np.max(np_array) - np.min(np_array))


def main():
    for length in [10**x for x in range(4, 8)]:
        numbers = generate_test_numbers(length)
        np_array = np.array(numbers)

        result = loop_norm(numbers)
        print(f"loop_norm@{length} check: {result[:5]}")

        result = norm(numbers)
        print(f"norm@{length} check: {result[:5]}")

        result = numpy_norm(np_array)
        print(f"numpy_norm@{length} check: {result[:5]}")


if __name__ == "__main__":
    main()
