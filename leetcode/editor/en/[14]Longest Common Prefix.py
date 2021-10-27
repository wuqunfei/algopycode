# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lower-case English letters. 
#  
#  Related Topics String 👍 5771 👎 2547


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


# o(M * N)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if i == len(strs[j]):
                    return strs[0][:i]
                if strs[j][i] != c:
                    return strs[0][:i]

        return strs[0]


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
x = solution.longestCommonPrefix(["flower", "flower", "flower", "flower"])
print(x)
