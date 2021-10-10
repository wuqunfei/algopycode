# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent. Return the answer in any order. 
# 
# 
#  A mapping of digit to letters (just like on the telephone buttons) is given 
# below. Note that 1 does not map to any letters. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  Example 2: 
# 
#  
# Input: digits = ""
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: digits = "2"
# Output: ["a","b","c"]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] is a digit in the range ['2', '9']. 
#  
#  Related Topics Hash Table String Backtracking 👍 7597 👎 586


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def __init__(self):
        self.letters = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}
        self.rev = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.generate(0, digits, '')
        return self.rev

    def generate(self, index: int, digits: str, str_value: str):
        # terminator
        if index == len(digits):
            self.rev.append(str_value)
            return
        # process
        group_letter = self.letters.get(digits[index])
        # recursion
        for j, char in enumerate(group_letter):
            self.generate(index + 1, digits, str_value + group_letter[j])

# leetcode submit region end(Prohibit modification and deletion)


# s = Solution()
# print(s.letterCombinations('23'))
