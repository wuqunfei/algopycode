# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics String Dynamic Programming Backtracking 👍 9911 👎 396


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def __init__(self):
        self.n: int = 0
        self.results: List[str] = []
        self.parentheses_left = '('
        self.parentheses_right = ')'

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        left, right, str_value = 0, 0, ''
        self.generator(left, right, str_value)
        return self.results

    def generator(self, left, right, str_value):
        if left == self.n and right == self.n:
            self.results.append(str_value)
            return
        else:
            if left < self.n:
                self.generator(left + 1, right, str_value + self.parentheses_left)
            elif left > right:
                self.generator(left, right + 1, str_value + self.parentheses_right)


s = Solution()
x = s.generateParenthesis(3)
print(x)
