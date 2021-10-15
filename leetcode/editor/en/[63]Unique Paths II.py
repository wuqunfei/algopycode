# A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
# the diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the 
# diagram below). 
# 
#  Now consider if some obstacles are added to the grids. How many unique paths 
# would there be? 
# 
#  An obstacle and space is marked as 1 and 0 respectively in the grid. 
# 
#  
#  Example 1: 
# 
#  
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#  
# 
#  Example 2: 
# 
#  
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] is 0 or 1. 
#  
#  Related Topics Array Dynamic Programming Matrix 👍 3637 👎 333


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)  # boundary
        columns = len(obstacleGrid[0])  # boundary
        states = [[0] * columns for _ in range(rows)]  # states defined

        for c in range(columns):
            if obstacleGrid[0][c] == 1: break
            states[0][c] = 1
        for r in range(rows):
            if obstacleGrid[r][0] == 1: break
            states[r][0] = 1

        for i in range(1, rows):
            for j in range(1, columns):  # mini iterate sub problem
                if obstacleGrid[i][j] == 1:
                    states[i][j] = 0
                else:
                    states[i][j] = states[i - 1][j] + states[i][j - 1]
        return states[- 1][- 1]


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.uniquePathsWithObstacles([[1, 0, 0], [0, 1, 0], [0, 0, 0]]))
