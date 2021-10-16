# You are given an integer array prices where prices[i] is the price of a given 
# stock on the iᵗʰ day. 
# 
#  On each day, you may decide to buy and/or sell the stock. You can only hold 
# at most one share of the stock at any time. However, you can buy it then 
# immediately sell it on the same day. 
# 
#  Find and return the maximum profit you can achieve. 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# 
# Total profit is 4 + 3 = 7.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 
# 5-1 = 4.
# Total profit is 4.
#  
# 
#  Example 3: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the 
# stock to achieve the maximum profit of 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 3 * 10⁴ 
#  0 <= prices[i] <= 10⁴ 
#  
#  Related Topics Array Dynamic Programming Greedy 👍 5599 👎 2207


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        size = len(prices)
        for i in range(size):
            if i + 1 < size and prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit

    # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/tan-xin-suan-fa-by-liweiwei1419-2/
    def max_dp(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [[0] * 2 for _ in range(days)]
        # 0: having cash
        # 1: having stock
        dp[0][0] = 0
        dp[0][1] = - prices[0]
        for i in range(1, days, 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[days - 1][0]


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.max_dp([7, 1, 5, 3, 6, 4]))
