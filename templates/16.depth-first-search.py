"""
Depth-First Search (DFS) Template
=================================

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Traversal | O(V + E) | O(H)  | Stack/Recursion (H=Height/Depth) |
| Path Finding | O(V + E) | O(H) | Can find any path |
| Cycle Detect | O(V + E) | O(V) | Using recursion stack |

Best Practices:
- **Recursion**: Simplest implementation.
- **Stack**: Iterative implementation to avoid recursion limit.
- **Backtracking**: DFS is the foundation of backtracking.
"""

from typing import List, Set, Any, Optional

# Definition for a binary tree node (used in examples)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DFSTemplate:
    """
    Encapsulates high-level generic template for DFS.
    """

    def solve(self, start_node: Any) -> List[Any]:
        """
        Generic DFS Template (Recursive).
        
        Steps:
        1. Initialize Visited set
        2. Call recursive helper
        3. Process node
        4. Recurse on neighbors
        """
        visited = set()
        result = []
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            result.append(node) # Process
            
            for neighbor in self._get_neighbors(node):
                dfs(neighbor)
                
        dfs(start_node)
        return result

    def _get_neighbors(self, node) -> List[Any]:
        """
        Abstraction for neighbors.
        """
        return [] # Placeholder


class DFSExamples:
    """
    Concrete examples of DFS patterns.
    """

    def max_area_of_island(self, grid: List[List[int]]) -> int:
        """
        Concrete Example: Max Area of Island (LeetCode 695).
        
        Pattern: Grid DFS to count connected components size.
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def dfs(r, c):
            if (r < 0 or r >= m or c < 0 or c >= n or 
                grid[r][c] == 0 or (r, c) in visited):
                return 0
            
            visited.add((r, c))
            area = 1
            # Visit 4 directions
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area

    def path_sum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Concrete Example: Path Sum (LeetCode 112).
        
        Pattern: Tree DFS.
        """
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
            
        return (self.path_sum(root.left, targetSum - root.val) or 
                self.path_sum(root.right, targetSum - root.val))

if __name__ == "__main__":
    # 2. Examples
    examples = DFSExamples()
    
    # Grid Example
    grid = [
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,0,0,0,0],
        [0,1,1,1,1]
    ]
    res_island = examples.max_area_of_island(grid)
    print(f"Example Result (Max Island): {res_island}") # 4
    
    # Tree Example
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8))
    res_path = examples.path_sum(root, 22) # 5 -> 4 -> 11 -> 2
    print(f"Example Result (Path Sum): {res_path}") # True
