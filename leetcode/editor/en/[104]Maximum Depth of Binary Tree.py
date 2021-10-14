# Given the root of a binary tree, return its maximum depth. 
# 
#  A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,2]
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: 0
#  
# 
#  Example 4: 
# 
#  
# Input: root = [0]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 49
# 58 👎 105


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.levels = set()
        self.visited = set()

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 1)
        return max(self.levels) if self.levels else 0

    def traverse(self, root: Optional[TreeNode], layer: int):
        if root:
            if root in self.visited:
                return
            self.visited.add(root)
            self.levels.add(layer)
            for node in [root.left, root.right]:
                if node not in self.visited:
                    self.traverse(root.left, layer + 1)
                    self.traverse(root.right, layer + 1)

# leetcode submit region end(Prohibit modification and deletion)
