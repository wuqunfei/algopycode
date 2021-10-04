# Given an integer array nums of unique elements, return all possible subsets (
# the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0]
# Output: [[],[0]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  All the numbers of nums are unique. 
#  
#  Related Topics Array Backtracking Bit Manipulation 👍 7173 👎 125


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

# https://leetcode-cn.com/problems/subsets/solution/hui-su-python-dai-ma-by-liweiwei1419/
# TODO DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for num in nums:
            new_sets = []
            for subset in sets:
                one_set = subset + [num]
                new_sets.append(one_set)
            sets.extend(new_sets)
        return sets


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.subsets([1, 2, 3]))
