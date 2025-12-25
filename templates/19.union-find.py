"""
Union Find (Disjoint Set Union) Template
========================================

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Find      | O(α(N)) | O(N) | α is Inverse Ackermann (nearly O(1)) |
| Union     | O(α(N)) | O(N) | Path Compression + Rank/Size |
| Connected | O(α(N)) | O(N) | Check if two nodes share root |

Best Practices:
- **Path Compression**: Point nodes directly to root during find.
- **Union by Rank/Size**: Attach smaller tree to larger tree to keep height low.
- **Components**: Count distinct roots to find number of connected components.
"""

from typing import List

class UnionFindTemplate:
    """
    Encapsulates high-level generic template for Union Find (DSU).
    """
    
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size # Number of connected components

    def find(self, x: int) -> int:
        """
        Find root with Path Compression.
        """
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) # Path compression
        return self.root[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union two sets by Rank. Returns True if successful (merged).
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            
            self.count -= 1
            return True
        return False

    def connected(self, x: int, y: int) -> bool:
        """
        Check connectivity.
        """
        return self.find(x) == self.find(y)


class UnionFindExamples:
    """
    Concrete examples of Union Find patterns.
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        """
        Concrete Example: Number of Connected Components (LeetCode 323).
        """
        dsu = UnionFindTemplate(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.count

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Concrete Example: Graph Valid Tree (LeetCode 261).
        Tree = Connected + No Cycles.
        """
        if len(edges) != n - 1:
            return False
            
        dsu = UnionFindTemplate(n)
        for u, v in edges:
            if not dsu.union(u, v): # Cycle detected
                return False
                
        return True

if __name__ == "__main__":
    # 2. Examples
    examples = UnionFindExamples()
    
    # Components
    edges = [[0, 1], [1, 2], [3, 4]]
    res_comps = examples.count_components(5, edges)
    print(f"Example Result (Components): {res_comps}") # 2
    
    # Valid Tree
    edges_tree = [[0, 1], [0, 2], [0, 3], [1, 4]]
    res_tree = examples.valid_tree(5, edges_tree)
    print(f"Example Result (Valid Tree): {res_tree}") # True
