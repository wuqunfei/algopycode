# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money. 
# 
#  Return the fewest number of coins that you need to make up that amount. If 
# that amount of money cannot be made up by any combination of the coins, return -1.
#  
# 
#  You may assume that you have an infinite number of each kind of coin. 
# 
#  
#  Example 1: 
# 
#  
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#  
# 
#  Example 2: 
# 
#  
# Input: coins = [2], amount = 3
# Output: -1
#  
# 
#  Example 3: 
# 
#  
# Input: coins = [1], amount = 0
# Output: 0
#  
# 
#  Example 4: 
# 
#  
# Input: coins = [1], amount = 1
# Output: 1
#  
# 
#  Example 5: 
# 
#  
# Input: coins = [1], amount = 2
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 2ยณยน - 1 
#  0 <= amount <= 10โด 
#  
#  Related Topics Array Dynamic Programming Breadth-First Search ๐ 8685 ๐ 225


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.coinChange([1, 2, 5], 11))
