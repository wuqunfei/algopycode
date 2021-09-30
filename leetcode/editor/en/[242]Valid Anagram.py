# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
#  Related Topics Hash Table String Sorting 👍 3304 👎 182

"""
O(N+N) -> 0(N) TC
O(N)
"""

# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# leetcode submit region end(Prohibit modification and deletion)
