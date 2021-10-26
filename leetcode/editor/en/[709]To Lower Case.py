# Given a string s, return the string after replacing every uppercase letter 
# with the same lowercase letter. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "Hello"
# Output: "hello"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "here"
# Output: "here"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "LOVELY"
# Output: "lovely"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 100 
#  s consists of printable ASCII characters. 
#  
#  Related Topics String 👍 857 👎 2143


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toLowerCase(self, s: str) -> str:
        to_lower = lambda x: chr(ord(x) | 32)
        is_upper = lambda x: 'A' <= x <= 'Z'
        return ''.join([to_lower(x) if is_upper(x) else x for x in s])
# leetcode submit region end(Prohibit modification and deletion)
