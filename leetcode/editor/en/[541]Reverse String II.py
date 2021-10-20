# Given a string s and an integer k, reverse the first k characters for every 2
# k characters counting from the start of the string. 
# 
#  If there are fewer than k characters left, reverse all of them. If there are 
# less than 2k but greater than or equal to k characters, then reverse the first 
# k characters and left the other as original. 
# 
#  
#  Example 1: 
#  Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#  Example 2: 
#  Input: s = "abcd", k = 2
# Output: "bacd"
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of only lowercase English letters. 
#  1 <= k <= 10⁴ 
#  
#  Related Topics Two Pointers String 👍 743 👎 1978


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)
        
# leetcode submit region end(Prohibit modification and deletion)
