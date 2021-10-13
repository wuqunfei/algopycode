# You are given a sorted array consisting of only integers where every element 
# appears exactly twice, except for one element which appears exactly once. 
# 
#  Return the single element that appears only once. 
# 
#  Your solution must run in O(log n) time and O(1) space. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
#  Example 2: 
#  Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁵ 
#  
#  Related Topics Array Binary Search 👍 3350 👎 90


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# https://leetcode-cn.com/problems/single-element-in-a-sorted-array/solution/er-fen-fa-wu-xu-shu-zu-ye-gua-yong-by-li-s6f2/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif mid % 2 == 1 and nums[mid] == nums[mid - 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
