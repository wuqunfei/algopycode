# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: s = "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: s = "{[]}"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 👍 9175 👎 363


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif char in parentheses.values():
                if stack == [] or parentheses[stack.pop()] != char:
                    return False
            else:
                return False
        return not stack


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.isValid("()[]{}"))
