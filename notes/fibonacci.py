from collections import defaultdict


def fib_rec(n: int):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_mem(n: int, memo: dict):  # Top -> Down
    if n <= 1:
        return n
    if memo[n] == 0:
        memo[n] = fib_mem(n - 1, memo) + fib_mem(n - 2, memo)
    return memo[n]


def fib_ds(n):  # Down -> Top
    dataset = [0, 1] + [None] * (n + 1)
    for i in range(2, n + 1):
        dataset[i] = dataset[i - 1] + dataset[i - 2]
    return dataset[n]


print(fib_rec(10))
print(fib_mem(10, defaultdict(int)))
print(fib_ds(10))
