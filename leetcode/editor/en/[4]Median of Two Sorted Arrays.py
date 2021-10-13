# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays. 
# 
#  The overall run time complexity should be O(log (m+n)). 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#  
# 
#  Example 3: 
# 
#  
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#  
# 
#  Example 4: 
# 
#  
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#  
# 
#  Example 5: 
# 
#  
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#  
# 
#  
#  Constraints: 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
#  Related Topics Array Binary Search Divide and Conquer 👍 12839 👎 1727


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        lines = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:  # reach the end of num1, add nums2  one by one with point
                lines.append(nums2[p2])
                p2 += 1
            elif p2 == n:  # reach the end or num2, add nums1 one by one with point
                lines.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                lines.append(nums1[p1])
                p1 += 1
            else:
                lines.append(nums2[p2])
                p2 += 1
        mid = len(lines) // 2
        if len(lines) % 2 == 1:
            return lines[mid]
        else:
            return (lines[mid] + lines[1]) / 2


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
