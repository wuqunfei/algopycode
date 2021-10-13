# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties: 
# 
#  
#  Integers in each row are sorted from left to right. 
#  The first integer of each row is greater than the last integer of the 
# previous row. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -10⁴ <= matrix[i][j], target <= 10⁴ 
#  
#  Related Topics Array Binary Search Matrix 👍 4730 👎 220


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

# TC: O(logN) * O(logN)
# SC: O(1)

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        row_left, row_right = 0, row - 1
        while row_left <= row_right:
            row_mid = row_left + (row_right - row_left) // 2
            row_values = matrix[row_mid]
            if row_values[0] <= target <= row_values[column - 1]:
                return self.locate(row_values, target)
            elif row_values[0] > target:
                row_right = row_mid - 1
            elif row_values[column - 1] < target:
                row_left = row_mid + 1
        return False

    def locate(self, row_values: List[int], target: int):
        length = len(row_values)
        # order array list
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if row_values[mid] == target:
                return True
            elif row_values[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))
