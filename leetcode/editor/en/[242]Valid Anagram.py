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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counters = {}
        for char in s:
            if char in counters:
                counters[char] += 1
            else:
                counters[char] = 1
        for char in t:
            if char in counters:
                counters[char] -= 1
                if counters[char] == 0:
                    del counters[char]
            else:
                return False
        return not counters

# leetcode submit region end(Prohibit modification and deletion)
