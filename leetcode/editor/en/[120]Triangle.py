# Given a triangle array, return the minimum path sum from top to bottom. 
# 
#  For each step, you may move to an adjacent number of the row below. More 
# formally, if you are on index i on the current row, you may move to either index i 
# or index i + 1 on the next row. 
# 
#  
#  Example 1: 
# 
#  
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined 
# above).
#  
# 
#  Example 2: 
# 
#  
# Input: triangle = [[-10]]
# Output: -10
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= triangle.length <= 200 
#  triangle[0].length == 1 
#  triangle[i].length == triangle[i - 1].length + 1 
#  -10⁴ <= triangle[i][j] <= 10⁴ 
#  
# 
#  
# Follow up: Could you do this using only O(n) extra space, where n is the 
# total number of rows in the triangle? Related Topics Array Dynamic Programming 👍 379
# 3 👎 354


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        return min(f)


# https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/

solution = Solution()
solution.minimumTotal([[-1], [2, 3], [1, -1, -3]])
# leetcode submit region end(Prohibit modification and deletion)
