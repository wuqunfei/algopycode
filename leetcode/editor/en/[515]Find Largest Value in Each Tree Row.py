# Given the root of a binary tree, return an array of the largest value in each 
# row of the tree (0-indexed). 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,3]
# Output: [1,3]
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,null,2]
# Output: [1,2]
#  
# 
#  Example 5: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree will be in the range [0, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 16
# 29 👎 74


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        states = collections.defaultdict(lambda: float('-inf'))
        self.generator(node=root, level=0, states=states)
        return states.values()

    def generator(self, node: TreeNode, level: int, states: dict):
        if node:
            states[level] = max(node.val, states[level])
            self.generator(node.left, level + 1, states)
            self.generator(node.right, level + 1, states)

# leetcode submit region end(Prohibit modification and deletion)
