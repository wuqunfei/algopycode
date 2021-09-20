# Given a string s, find the first non-repeating character in it and return its 
# index. If it does not exist, return -1. 
# 
#  
#  Example 1: 
#  Input: s = "leetcode"
# Output: 0
#  Example 2: 
#  Input: s = "loveleetcode"
# Output: 2
#  Example 3: 
#  Input: s = "aabb"
# Output: -1
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of only lowercase English letters. 
#  
#  Related Topics Hash Table String Queue Counting 👍 3562 👎 166


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for index, char in enumerate(s):
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        for index, char in enumerate(s):
            if char_dict.get(char) == 1:
                return index
        return -1

# leetcode submit region end(Prohibit modification and deletion)
