# You are given an integer array cost where cost[i] is the cost of iᵗʰ step on 
# a staircase. Once you pay the cost, you can either climb one or two steps. 
# 
#  You can either start from the step with index 0, or the step with index 1. 
# 
#  Return the minimum cost to reach the top of the floor. 
# 
#  
#  Example 1: 
# 
#  
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
#  
# 
#  Example 2: 
# 
#  
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping 
# cost[3].
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= cost.length <= 1000 
#  0 <= cost[i] <= 999 
#  
#  Related Topics Array Dynamic Programming 👍 4458 👎 875


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n  # costs
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]  # transition
        return min(dp[- 1], dp[n - 2])


solution = Solution()
print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# leetcode submit region end(Prohibit modification and deletion)
