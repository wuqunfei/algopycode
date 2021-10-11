# A gene string can be represented by an 8-character long string, with choices 
# from 'A', 'C', 'G', and 'T'. 
# 
#  Suppose we need to investigate a mutation from a gene string start to a gene 
# string end where one mutation is defined as one single character changed in the 
# gene string. 
# 
#  
#  For example, "AACCGGTT" --> "AACCGGTA" is one mutation. 
#  
# 
#  There is also a gene bank bank that records all the valid gene mutations. A 
# gene must be in bank to make it a valid gene string. 
# 
#  Given the two gene strings start and end and the gene bank bank, return the 
# minimum number of mutations needed to mutate from start to end. If there is no 
# such a mutation, return -1. 
# 
#  Note that the starting point is assumed to be valid, so it might not be 
# included in the bank. 
# 
#  
#  Example 1: 
# 
#  
# Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA",
# "AAACGGTA"]
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC",
# "AACCCCCC"]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  start.length == 8 
#  end.length == 8 
#  0 <= bank.length <= 10 
#  bank[i].length == 8 
#  start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T']. 
# 
#  
#  Related Topics Hash Table String Breadth-First Search 👍 671 👎 81


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank: return -1
        queue = collections.deque([(start, 0)])
        dna = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while queue:
            node, count = queue.popleft()
            if node == end:
                return count
            for i, v in enumerate(node):
                for j in dna[v]:
                    new_node = node[:i] + j + node[i + 1:]
                    if new_node in bank:
                        queue.append((new_node, count + 1))
                        bank.remove(new_node)
        return -1


# leetcode submit region end(Prohibit modification and deletion)
solution = Solution()
solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
