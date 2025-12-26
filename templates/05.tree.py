"""
Binary Tree Template
====================

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access    | O(N) | O(H)  | DFS traversal (H=Height) |
| Search    | O(N) | O(H)  | O(log N) if BST and balanced |
| Insertion | O(N) | O(H)  | Level order or BST insert |
| Deletion  | O(N) | O(H)  | Complex in BST |

Best Practices:
- **Recursion**: Most tree problems are solved recursively.
- **Base Case**: Always handle `if not root: return ...`.
- **Traversals**: Know DFS (Pre/In/Post) and BFS (Level Order).
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class TreePatterns:
    """
    Encapsulates common patterns and operations for Binary Trees.
    """

    def create_bst(self, values: List[int]) -> Optional[TreeNode]:
        """
        Helper to create a simple BST from list (for testing).
        """
        root = None
        for val in values:
            root = self._insert_into_bst(root, val)
        return root

    def _insert_into_bst(self, root: Optional[TreeNode], val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self._insert_into_bst(root.left, val)
        else:
            root.right = self._insert_into_bst(root.right, val)
        return root

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS: Root -> Left -> Right.
        """
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS: Left -> Root -> Right (Sorted order for BST).
        """
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS: Left -> Right -> Root (Bottom-up).
        """
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res

    def level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS: Level by level using Queue.
        """
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level_vals = []
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_vals)
        return res

    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate maximum depth (height) of tree.
        """
        if not root:
            return 0
        left_h = self.max_depth(root.left)
        right_h = self.max_depth(root.right)
        return max(left_h, right_h) + 1

if __name__ == "__main__":
    solver = TreePatterns()
    
    # 1. Create
    root = solver.create_bst([4, 2, 6, 1, 3, 5, 7])
    
    # 2. Traversals
    pre = solver.preorder_traversal(root) # [4, 2, 1, 3, 6, 5, 7]
    in_order = solver.inorder_traversal(root) # [1, 2, 3, 4, 5, 6, 7]
    post = solver.postorder_traversal(root) # [1, 3, 2, 5, 7, 6, 4]
    levels = solver.level_order_traversal(root) # [[4], [2, 6], [1, 3, 5, 7]]
    
    # 3. Depth
    depth = solver.max_depth(root) # 3
