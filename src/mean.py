import numpy as np

from decorators import profile
from utils import generate_test_numbers


@profile
def loop_mean(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1

    return total / count


@profile
def mean(numbers):
    return sum(numbers) / len(numbers)


@profile
def numpy_mean(np_array):
    return np.mean(np_array)


def main():
    for length in [10**x for x in range(4, 8)]:
        numbers = generate_test_numbers(length)
        np_array = np.array(numbers)

        result = loop_mean(numbers)
        print(f"loop_mean@{length}: {result}")

        result = mean(numbers)
        print(f"mean@{length}: {result}")

        result = numpy_mean(np_array)
        print(f"numpy_mean@{length}: {result}")


if __name__ == "__main__":
    main()
