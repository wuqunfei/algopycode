# Given the root of a binary tree, return the inorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
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
# Input: root = [1,2]
# Output: [2,1]
#  
# 
#  Example 5: 
# 
#  
# Input: root = [1,null,2]
# Output: [1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Recursive solution is trivial, could you do it iteratively? 
# Related Topics Stack Tree Depth-First Search Binary Tree 👍 5811 👎 245


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


"""
0(N)  Time C = 2 * T(n/2) +1
0(N)  Space C

Next time stack 
"""

class Solution:
    def __init__(self):
        self.rev = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.rev

    def traversal(self, root: Optional[TreeNode]) -> None:
        if root:
            self.inorderTraversal(root.left)
            if root.val:
                self.rev.append(root.val)
            self.inorderTraversal(root.right)

# leetcode submit region end(Prohibit modification and deletion)
