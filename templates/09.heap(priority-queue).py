"""
Heap (Priority Queue) Template
==============================

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Push      | O(log N) | O(1)  | `heapq.heappush()` |
| Pop       | O(log N) | O(1)  | `heapq.heappop()` (Min element) |
| Peek      | O(1)     | O(1)  | `heap[0]` (Min element) |
| Heapify   | O(N)     | O(1)  | `heapq.heapify()` |

Best Practices:
- **Min-Heap**: Python's `heapq` implements a Min-Heap by default.
- **Max-Heap**: Simulate Max-Heap by pushing negative values (e.g., `-val`).
- **Top K**: Use `heapq.nlargest` or `heapq.nsmallest` (O(N log K)).
- **Merge**: Efficiently merge sorted lists.
"""

import heapq
from typing import List, Any

class HeapPatterns:
    """
    Encapsulates common patterns and operations for Heaps (Priority Queues).
    """

    def initialization(self) -> List[int]:
        """
        Initialize an empty heap.
        """
        return []

    def push(self, heap: List[int], val: int) -> None:
        """
        Push element onto heap.
        
        Complexity: O(log N)
        """
        heapq.heappush(heap, val)

    def pop(self, heap: List[int]) -> int:
        """
        Pop smallest element from heap.
        
        Complexity: O(log N)
        """
        if not heap:
            raise IndexError("pop from empty heap")
        return heapq.heappop(heap)

    def peek(self, heap: List[int]) -> int:
        """
        Peek at smallest element.
        
        Complexity: O(1)
        """
        if not heap:
            raise IndexError("peek at empty heap")
        return heap[0]

    def create_heap(self, nums: List[int]) -> List[int]:
        """
        Convert list to heap in-place.
        
        Complexity: O(N)
        """
        heapq.heapify(nums)
        return nums

    def find_kth_largest(self, nums: List[int], k: int) -> int:
        """
        Find Kth largest element using Min-Heap of size K.
        
        Complexity: O(N log K)
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def find_kth_largest_optimized(self, nums: List[int], k: int) -> int:
        """
        Find Kth largest using built-in nlargest.
        
        Complexity: O(N log K)
        """
        return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":
    solver = HeapPatterns()
    
    # 1. Basic Ops
    min_heap = []
    solver.push(min_heap, 3)
    solver.push(min_heap, 1)
    solver.push(min_heap, 5)
    
    peek_val = solver.peek(min_heap) # 1
    pop_val = solver.pop(min_heap)   # 1
    
    # 2. Heapify
    arr = [3, 1, 5, 2]
    solver.create_heap(arr) # [1, 2, 5, 3] (approximately)
    
    # 3. Patterns
    kth = solver.find_kth_largest([3, 2, 1, 5, 6, 4], 2) # 5
