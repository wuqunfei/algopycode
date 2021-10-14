# Serialization is the process of converting a data structure or object into a 
# sequence of bits so that it can be stored in a file or memory buffer, or 
# transmitted across a network connection link to be reconstructed later in the same or 
# another computer environment. 
# 
#  Design an algorithm to serialize and deserialize a binary tree. There is no 
# restriction on how your serialization/deserialization algorithm should work. You 
# just need to ensure that a binary tree can be serialized to a string and this 
# string can be deserialized to the original tree structure. 
# 
#  Clarification: The input/output format is the same as how LeetCode 
# serializes a binary tree. You do not necessarily need to follow this format, so please be 
# creative and come up with different approaches yourself. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
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
# Output: [1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics String Tree Depth-First Search Breadth-First Search Design 
# Binary Tree 👍 5278 👎 223


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'X'

        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return f'{root.val},{left},{right}'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        datasets = collections.deque(data.split(','))

        def build(sets):
            if len(sets) == 0:
                return None
            node_str = sets.popleft()
            if node_str == 'X':
                return None
            node = TreeNode(int(node_str))
            node.left = build(sets)
            node.right = build(sets)
            return node
        tree = build(datasets)
        return tree

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)

# TODO: bugs in the complie