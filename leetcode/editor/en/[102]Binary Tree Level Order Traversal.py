# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
#  Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
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
#  -1000 <= Node.val <= 1000
#
#  Related Topics Tree Breadth-First Search Binary Tree 👍 6038 👎 128


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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        states = collections.defaultdict(list)
        self.generate(root, 0, states)
        return states.values()

    def generate(self, root, level, states):
        if root:
            states[level].append(root.val)
            self.generate(root.left, level + 1, states)
            self.generate(root.right, level + 1, states)

# leetcode submit region end(Prohibit modification and deletion)
