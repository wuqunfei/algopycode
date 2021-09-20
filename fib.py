from typing import List
from collections import deque


def fib(n: int, memo=None):
    result = None
    if memo is not None:
        result = memo[n]
        if result is not None:
            return result
    if n < 0:
        raise Exception('N is Incorrect')
    elif n == 0:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    if memo is not None:
        memo[n] = result
    return result


def fib_ds(n):
    dataset = [0, 1] + [None] * (n + 1)
    for i in range(2, n + 1):
        dataset[i] = dataset[i - 1] + dataset[i - 2]
    return dataset[n]


# print(fib(1000, [None] * (1000 + 1)))
print(fib(10))
