# Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
# '0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 10505 👎 274


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# https://zh.wikipedia.org/wiki/Flood_fill

class Solution:
    def __init__(self):
        self.row = 0
        self.column = 0
        self.grid = []

    def numIslands(self, grid: [[str]]) -> int:
        amount = 0

        self.row = len(grid)
        self.column = len(grid[0])
        self.grid = grid

        for x in range(self.row):
            for y in range(self.column):
                if self.grid[x][y] == '1':
                    self.dfs(x, y)
                    amount += 1
        return amount

    def dfs(self, x, y):
        if not 0 <= x < self.row or not 0 <= y < self.column or self.grid[x][y] == '0':
            return
        self.grid[x][y] = '0'
        self.dfs(x + 1, y)
        self.dfs(x, y + 1)
        self.dfs(x - 1, y)
        self.dfs(x, y - 1)

# leetcode submit region end(Prohibit modification and deletion)
# solution = Solution()
# x = solution.numIslands([["1", "1", "1", "1", "0"],
#                          ["1", "1", "0", "1", "0"],
#                          ["1", "1", "0", "0", "0"],
#                          ["0", "0", "0", "0", "0"]])
# print(x)
