# Write a function that reverses a string. The input string is given as an 
# array of characters s. 
# 
#  
#  Example 1: 
#  Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#  Example 2: 
#  Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is a printable ascii character. 
#  
# 
#  
#  Follow up: Do not allocate extra space for another array. You must do this 
# by modifying the input array in-place with O(1) extra memory. 
#  Related Topics Two Pointers String Recursion 👍 3188 👎 840


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


# leetcode submit region end(Prohibit modification and deletion)

solution = Solution()
print(solution.reverseString(["h", "e", "l", "l", "o"]))
