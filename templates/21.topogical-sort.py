"""
Topological Sort Template
=========================

Complexity Summary
------------------
| Algorithm | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Kahn's (BFS) | O(V+E)| O(V)  | Detects cycles (nodes processed < V) |
| DFS       | O(V+E)   | O(V)  | Reverse post-order |

Best Practices:
- **DAG Only**: Only works on Directed Acyclic Graphs.
- **Indegree**: Core concept for Kahn's algorithm (Dependencies).
- **Cycle Detection**: If result length != V, graph has cycle.
"""

from typing import List, Dict
from collections import deque, defaultdict

class TopologicalSortTemplate:
    """
    Encapsulates high-level generic template for Topological Sort.
    """

    def solve_kahns(self, num_nodes: int, edges: List[List[int]]) -> List[int]:
        """
        Kahn's Algorithm (BFS Based).
        
        Steps:
        1. Build Graph and Indegree map
        2. Push 0-indegree nodes to Queue
        3. Process Queue:
           - Add node to result
           - Decrement neighbor indegrees
           - If neighbor indegree becomes 0, push to Queue
        """
        # 1. Build Graph
        graph = defaultdict(list)
        indegree = {i: 0 for i in range(num_nodes)}
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
            
        # 2. Init Queue
        queue = deque([node for node in indegree if indegree[node] == 0])
        result = []
        
        # 3. Process
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return result if len(result) == num_nodes else [] # Empty if cycle


class TopologicalSortExamples:
    """
    Concrete examples of Topological Sort patterns.
    """

    def find_order(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Concrete Example: Course Schedule II (LeetCode 210).
        """
        # Prerequisites are [course, pre], so edge pre -> course
        edges = [[pre, course] for course, pre in prerequisites]
        
        solver = TopologicalSortTemplate()
        return solver.solve_kahns(numCourses, edges)

if __name__ == "__main__":
    # 2. Examples
    examples = TopologicalSortExamples()
    
    # Course Schedule: 4 courses, [1,0], [2,0], [3,1], [3,2]
    # 0 -> 1 -> 3
    # 0 -> 2 -> 3
    prereqs = [[1,0], [2,0], [3,1], [3,2]]
    res_order = examples.find_order(4, prereqs)
    print(f"Example Result (Course Schedule): {res_order}") # [0, 1, 2, 3] or [0, 2, 1, 3]
