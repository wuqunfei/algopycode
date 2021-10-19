from typing import List


def dp(data: List):
    n = len(data)
    states = [0] * n
    # create state,
    dp[0] = 1
    # init value
    for i in range(1, n):
        # boundary and ignore first one, direction top->down, left-right
        if True:
            # Meet Condition
            dp[i] = transition(dp[i - 1])
            # transition equation
    return dp[-1]
    # return the answer of requirement


def transition(x):
    # find the core state change of the question
    return x + 1
