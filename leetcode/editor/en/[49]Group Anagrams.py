# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  Example 2: 
#  Input: strs = [""]
# Output: [[""]]
#  Example 3: 
#  Input: strs = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lowercase English letters. 
#  
#  Related Topics Hash Table String Sorting 👍 6940 👎 255


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rev = collections.defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
            rev[key].append(str)
        return rev.values()


# leetcode submit region end(Prohibit modification and deletion)
