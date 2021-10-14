# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the 
# root node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁵]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 31
# 30 👎 877


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            min_depth = 10 ** 5
            if root.left:
                min_depth = min(self.minDepth(root.left), min_depth)
            if root.right:
                min_depth = min(self.minDepth(root.right), min_depth)
            return min_depth + 1

# leetcode submit region end(Prohibit modification and deletion)
