# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day, and an integer fee representing a transaction fee. 
# 
#  Find the maximum profit you can achieve. You may complete as many 
# transactions as you like, but you need to pay the transaction fee for each transaction. 
# 
#  Note: You may not engage in multiple transactions simultaneously (i.e., you 
# must sell the stock before you buy again). 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 5 * 10⁴ 
#  1 <= prices[i] < 5 * 10⁴ 
#  0 <= fee < 5 * 10⁴ 
#  
#  Related Topics Array Dynamic Programming Greedy 👍 3145 👎 84


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        days = len(prices)
        dp = [[0] * 2 for _ in range(days)]
        # 0: having cash
        # 1: having stock
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        for i in range(1, days, 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[days - 1][0]

# leetcode submit region end(Prohibit modification and deletion)
