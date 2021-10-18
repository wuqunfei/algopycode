# Given an integer array nums, find a contiguous non-empty subarray within the 
# array that has the largest product, and return the product. 
# 
#  It is guaranteed that the answer will fit in a 32-bit integer. 
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer. 
#  
#  Related Topics Array Dynamic Programming 👍 8588 👎 266


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def max_dp(self, nums):
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        total = nums[0]
        for i in range(1, n):
            v = nums[i]
            values = [dp[i - 1][0] * v, dp[i - 1][1] * v, v]
            dp[i][0] = min(values)
            dp[i][1] = max(values)
            total = max(dp[i][1], total)
        return total


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.max_dp([-2, 3, -4]))
