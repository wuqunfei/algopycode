from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [0] + [float('inf')] * amount
        for coin in coins:
            for x in range(coin, amount + 1):
                f[x] = min(f[x], f[x - coin] + 1)
        if f[amount] != float('inf'):
            return f[amount]
        else:
            return -1


solution = Solution()
x = solution.coinChange([1, 2, 5], 11)
print(x)
