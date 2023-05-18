import random

random.seed(123)


def generate_test_numbers(length):
    return [int(100 * random.random()) for _ in range(length)]
