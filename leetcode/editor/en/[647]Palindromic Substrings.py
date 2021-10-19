# Given a string s, return the number of palindromic substrings in it. 
# 
#  A string is a palindrome when it reads the same backward as forward. 
# 
#  A substring is a contiguous sequence of characters within the string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists of lowercase English letters. 
#  
#  Related Topics String Dynamic Programming 👍 5231 👎 144


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        rev = 0
        dp = [[False] * size for _ in range(size)]

        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                if s[i] == s[j]:
                    dp[i][j] = j - i <= 2 or dp[i + 1][j - 1]
                    if dp[i][j]:
                        rev += 1
        return rev


# inspire https://leetcode-cn.com/problems/palindromic-substrings/solution/shu-ju-jie-gou-he-suan-fa-dong-tai-gui-h-3bms/


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
print(solution.countSubstrings('aba'))
