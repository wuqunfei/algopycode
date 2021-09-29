# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics Math Dynamic Programming Memoization 👍 8264 👎 241


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Optional


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        states: List[Optional[int]] = [None] * n
        states[0] = 1
        states[1] = 2
        for i in range(2, n):
            states[i] = states[i - 1] + states[i - 2]
        return states[n - 1]


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
x = s.climbStairs(4)
print(x)
