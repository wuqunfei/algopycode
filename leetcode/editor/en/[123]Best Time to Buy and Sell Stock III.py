# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day. 
# 
#  Find the maximum profit you can achieve. You may complete at most two 
# transactions. 
# 
#  Note: You may not engage in multiple transactions simultaneously (i.e., you 
# must sell the stock before you buy again). 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you 
# are engaging multiple transactions at the same time. You must sell before buying 
# again.
#  
# 
#  Example 3: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#  
# 
#  Example 4: 
# 
#  
# Input: prices = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁵ 
#  
#  Related Topics Array Dynamic Programming 👍 4613 👎 100


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/123-mai-mai-gu-piao-de-zui-jia-shi-ji-ii-zfh9/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0:
            return 0
        # dp[][x] state
        # 0: no operation 1. 1st buy 2. 1st sell 3. 2nd buy 4. 2nd sell
        dp = [[0] * 5 for _ in range(size)]
        dp[0][1] = - prices[0]
        dp[0][3] = - prices[0]
        for i in range(1, size):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
        return dp[-1][4]


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.maxProfit([1, 2, 3, 4, 5]))
