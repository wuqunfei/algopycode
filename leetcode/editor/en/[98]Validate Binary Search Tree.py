# Given the root of a binary tree, determine if it is a valid binary search 
# tree (BST). 
# 
#  A valid BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the 
# node's key. 
#  The right subtree of a node contains only nodes with keys greater than the 
# node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: root = [2,1,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 7547
#  👎 769


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.queue = collections.deque()

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                    validate(node.left, low, node.val))

        return validate(root)

# leetcode submit region end(Prohibit modification and deletion)
