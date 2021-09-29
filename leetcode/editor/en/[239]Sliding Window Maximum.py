# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
#  
# 
#  Example 4: 
# 
#  
# Input: nums = [9,11], k = 2
# Output: [11]
#  
# 
#  Example 5: 
# 
#  
# Input: nums = [4,-2], k = 2
# Output: [4]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic 
# Queue 👍 7396 👎 268


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque

"""
Time O(N)
Space O(3)
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        rev = []
        dq = deque()
        for i in range(n):
            """
            Remove until less the new value
            """
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

            """
            Remove left if queue length > 3
            """
            while dq and i - dq[0] >= k:
                dq.popleft()

            """
            Add value only index  > 2 windows size 
            """
            if i >= k - 1:
                rev.append(nums[dq[0]])

        return rev


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
