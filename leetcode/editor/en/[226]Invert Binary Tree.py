# Given the root of a binary tree, invert the tree, and return its root. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,1,3]
# Output: [2,3,1]
#  
# 
#  Example 3: 
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
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 64
# 30 👎 90


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
        self.queue = collections.deque()

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

# leetcode submit region end(Prohibit modification and deletion)
