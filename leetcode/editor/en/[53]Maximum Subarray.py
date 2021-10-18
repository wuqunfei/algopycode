# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum and return its sum. 
# 
#  A subarray is a contiguous part of an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle. 
#  Related Topics Array Divide and Conquer Dynamic Programming 👍 15304 👎 714


# leetcode submit region begin(Prohibit modification and deletion)
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        total = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            total = max(dp[i], total)
        return total
# leetcode submit region end(Prohibit modification and deletion)