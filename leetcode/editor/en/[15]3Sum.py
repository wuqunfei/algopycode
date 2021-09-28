# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics Array Two Pointers Sorting 👍 13200 👎 1278


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

"""
 Not O
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return list(res)


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
x = s.threeSum([-1, 0, 1, 2, -1, -4])
print(x)
