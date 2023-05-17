import random

random.seed(123)


def build_test_list(length):
    return [int(100 * random.random()) for _ in range(length)]
