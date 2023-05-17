import random

random.seed(123)

def build_test_arr(length):
    return [int(100 * random.random()) for _ in range(length)]

