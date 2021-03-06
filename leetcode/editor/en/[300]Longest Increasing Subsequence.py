# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence. 
# 
#  A subsequence is a sequence that can be derived from an array by deleting 
# some or no elements without changing the order of the remaining elements. For 
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
# complexity? 
#  Related Topics Array Binary Search Dynamic Programming 👍 9215 👎 190


# leetcode submit region begin(Prohibit modification and deletion)
import bisect
from typing import List


# TC: O(N * N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        dp = [1] * length
        rev = 0
        for i in range(1, length):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            rev = max(rev, dp[i])
        return rev

    # https: // leetcode - cn.com / problems / longest - increasing - subsequence / solution / zui - chang - shang - sheng - zi - xu - lie - dong - tai - gui - hua - 2 /
    def binaryLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            i = bisect.bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)

        # leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
x = solution.binaryLIS([0, 1, 0, 3, 1])
print(x)
