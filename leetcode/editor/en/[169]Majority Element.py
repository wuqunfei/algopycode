# Given an array nums of size n, return the majority element. 
# 
#  The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array. 
# 
#  
#  Example 1: 
#  Input: nums = [3,2,3]
# Output: 3
#  Example 2: 
#  Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 5 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
# 
#  
# Follow-up: Could you solve the problem in linear time and in O(1) space? 
# Related Topics Array Hash Table Divide and Conquer Sorting Counting 👍 6610 👎 291


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


# leetcode submit region end(Prohibit modification and deletion)
#
# s = Solution()
# print(s.majorityElement([3, 2, 3]))
