# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return all distinct solutions to the n-queens puzzle. 
# You may return the answer in any order. 
# 
#  Each solution contains a distinct board configuration of the n-queens' 
# placement, where 'Q' and '.' both indicate a queen and an empty space, respectively. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as 
# shown above
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [["Q"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Array Backtracking 👍 4237 👎 129


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def __init__(self):
        self.rev = []
        self.n = 0
        self.columns = set()
        self.hypotenuse_45 = set()
        self.hypotenuse_45_reverse = set()

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.dfs(0, [])
        return self.generate()

    def dfs(self, row, state):
        if row >= self.n:
            self.rev.append(state)
            return

        for column in range(self.n):
            if column in self.columns or \
                    row + column in self.hypotenuse_45 or \
                    row - column in self.hypotenuse_45_reverse:
                continue

            self.set_state(column, row)
            self.dfs(row + 1, state + [column])
            self.reset_state(column, row)

    def set_state(self, column, row):
        self.columns.add(column)
        self.hypotenuse_45.add(row + column)
        self.hypotenuse_45_reverse.add(row - column)

    def reset_state(self, column, row):
        self.columns.remove(column)
        self.hypotenuse_45.remove(row + column)
        self.hypotenuse_45_reverse.remove(row - column)

    def generate(self):
        ds = []
        for x in self.rev:
            matrix = []
            for i in x:
                matrix.append('.' * i + 'Q' + '.' * (self.n - i - 1))
            ds.append(matrix)
        return ds


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.solveNQueens(4))
