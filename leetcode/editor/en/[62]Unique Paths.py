# A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
# the diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the 
# diagram below). 
# 
#  How many possible unique paths are there? 
# 
#  
#  Example 1: 
# 
#  
# Input: m = 3, n = 7
# Output: 28
#  
# 
#  Example 2: 
# 
#  
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-
# right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#  
# 
#  Example 3: 
# 
#  
# Input: m = 7, n = 3
# Output: 28
#  
# 
#  Example 4: 
# 
#  
# Input: m = 3, n = 3
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 100 
#  It's guaranteed that the answer will be less than or equal to 2 * 10⁹. 
#  
#  Related Topics Math Dynamic Programming Combinatorics 👍 6587 👎 261


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        states = [[0] * n for _ in range(m)] # column and row exchange to init

        for x in range(m):
            for y in range(n):
                if x == 0 or y == 0:
                    states[x][y] = 1   # edage is 1, there is no another way
                else:
                    states[x][y] = states[x - 1][y] + states[x][y - 1]
        return states[m - 1][n - 1]


solution = Solution()
print(solution.uniquePaths(3, 2))
