# Implement strStr(). 
# 
#  Return the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great 
# question to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty 
# string. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
#  Input: haystack = "hello", needle = "ll"
# Output: 2
#  Example 2: 
#  Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  Example 3: 
#  Input: haystack = "", needle = ""
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  0 <= haystack.length, needle.length <= 5 * 10⁴ 
#  haystack and needle consist of only lower-case English characters. 
#  
#  Related Topics Two Pointers String String Matching 👍 3069 👎 2896


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def kmp(pattern):
            prev, prefix = 0, [0]
            for i in range(1, len(pattern)):
                while prev > 0 and pattern[i] != pattern[prev]:
                    prev = prefix[prev - 1]
                if pattern[prev] == pattern[i]:
                    prev += 1
                else:
                    prev = 0
                prefix.append(prev)
            return prefix

        prefix = kmp(needle + '#' + haystack)
        length = len(needle)
        if length == 0:
            return length
        for i in range(length + 1, len(prefix)):
            if prefix[i] == length:
                return i - 2 * length
        return -1


# leetcode submit region end(Prohibit modification and deletion)


solution = Solution()
print(solution.strStr('aabaabaaf', 'aabaaf'))
