"""
Graph Template
==============

Complexity Summary
------------------
| Operation | Time      | Space    | Notes |
|-----------|-----------|----------|-------|
| Add Node  | O(1)      | O(1)     | |
| Add Edge  | O(1)      | O(1)     | Adjacency List |
| BFS       | O(V + E)  | O(V)     | Shortest Path (Unweighted) |
| DFS       | O(V + E)  | O(V)     | Traversal, Cycle Detection |

Best Practices:
- **Representation**: Adjacency List (Dict of Sets/Lists) is standard for sparse graphs.
- **BFS**: Use `collections.deque`.
- **DFS**: Use recursion or stack.
- **Visited Set**: Crucial to prevent cycles and redundant processing.
"""

from typing import Dict, List, Set, Any
from collections import deque, defaultdict

class GraphPatterns:
    """
    Encapsulates common patterns and operations for Graphs.
    """

    def build_graph(self, edges: List[List[int]]) -> Dict[int, List[int]]:
        """
        Build undirected graph from edge list.
        
        Complexity: O(E)
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def bfs(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Breadth-First Search.
        
        Complexity: O(V + E)
        """
        visited = {start}
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs_iterative(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Depth-First Search (Iterative).
        
        Complexity: O(V + E)
        """
        visited = {start}
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node)
            
            for neighbor in reversed(graph[node]): # Reverse to match recursive order usually
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return result

    def dfs_recursive(self, graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        Depth-First Search (Recursive).
        
        Complexity: O(V + E)
        """
        visited = set()
        result = []
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                dfs(neighbor)
                
        dfs(start)
        return result

    def shortest_path_bfs(self, graph: Dict[int, List[int]], start: int, target: int) -> int:
        """
        Find shortest path in unweighted graph using BFS.
        
        Complexity: O(V + E)
        """
        queue = deque([(start, 0)])
        visited = {start}
        
        while queue:
            node, dist = queue.popleft()
            if node == target:
                return dist
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return -1

if __name__ == "__main__":
    solver = GraphPatterns()
    
    # 1. Build Graph
    # 0 -- 1
    # |    |
    # 2 -- 3
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    g = solver.build_graph(edges)
    
    # 2. Traversals
    bfs_res = solver.bfs(g, 0)      # [0, 1, 2, 3] (order may vary)
    dfs_res = solver.dfs_recursive(g, 0) # [0, 1, 3, 2] (order may vary)
    
    # 3. Shortest Path
    dist = solver.shortest_path_bfs(g, 0, 3) # 2
