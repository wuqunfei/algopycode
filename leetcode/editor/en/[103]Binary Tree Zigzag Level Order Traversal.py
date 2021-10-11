# Given the root of a binary tree, return the zigzag level order traversal of 
# its nodes' values. (i.e., from left to right, then right to left for the next 
# level and alternate between). 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: [[1]]
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
#  The number of nodes in the tree is in the range [0, 2000]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Breadth-First Search Binary Tree 👍 4377 👎 144


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        states = collections.defaultdict(collections.deque)
        left_right = True
        self.generate(node=root, level=0, states=states, direction=left_right)
        return states.values()

    def generate(self, node: TreeNode, level, states, direction):
        if node:
            if direction:
                states[level].append(node.val)
            else:
                states[level].appendleft(node.val)
            self.generate(node.left, level + 1, states, not direction)
            self.generate(node.right, level + 1, states, not direction)


# leetcode submit region end(Prohibit modification and deletion)
