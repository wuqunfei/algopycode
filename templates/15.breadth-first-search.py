"""
Breadth-First Search (BFS) Template
===================================

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Traversal | O(V + E) | O(V)  | Queue based |
| Shortest Path | O(V + E) | O(V) | Unweighted graphs |
| Level Order | O(N) | O(W) | W = max width of tree |

Best Practices:
- **Queue**: Use `collections.deque`.
- **Visited**: Essential for graphs to avoid cycles.
- **Level-by-Level**: Use inner loop `for _ in range(len(queue))` to track levels.
"""

from typing import List, Deque, Set, Optional
from collections import deque

# Definition for a binary tree node (used in examples)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BFSTemplate:
    """
    Encapsulates high-level generic template for BFS.
    """

    def solve(self, start_node: Any) -> List[Any]:
        """
        Generic BFS Template.
        
        Steps:
        1. Initialize Queue with start node
        2. Initialize Visited set
        3. Loop while queue is not empty
        4. Process current node
        5. Add unvisited neighbors to queue
        """
        if not start_node:
            return []
            
        queue = deque([start_node])
        visited = {start_node}
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in self._get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result

    def _get_neighbors(self, node) -> List[Any]:
        """
        Abstraction for getting neighbors (Graph or Tree).
        """
        return [] # Placeholder


class BFSExamples:
    """
    Concrete examples of BFS patterns.
    """

    def level_order_traversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Concrete Example: Binary Tree Level Order Traversal (LeetCode 102).
        
        Pattern: Level-by-level BFS.
        """
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(current_level)
            
        return result

    def shortest_path_binary_matrix(self, grid: List[List[int]]) -> int:
        """
        Concrete Example: Shortest Path in Binary Matrix (LeetCode 1091).
        Find shortest path from (0,0) to (n-1,n-1). 0 is clear, 1 is blocked.
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
            
        queue = deque([(0, 0, 1)]) # (r, c, dist)
        visited = {(0, 0)}
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        while queue:
            r, c, dist = queue.popleft()
            
            if r == n - 1 and c == n - 1:
                return dist
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
                    
        return -1

if __name__ == "__main__":
    # 2. Examples
    examples = BFSExamples()
    
    # Tree Example
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    res_level = examples.level_order_traversal(root)
    print(f"Example Result (Level Order): {res_level}") # [[3], [9, 20], [15, 7]]
    
    # Grid Example
    grid = [[0,1],[1,0]]
    res_path = examples.shortest_path_binary_matrix(grid)
    print(f"Example Result (Shortest Path): {res_path}") # 2
