"""
Queue Template
==============

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Enqueue   | O(1) | O(1)  | `deque.append()` |
| Dequeue   | O(1) | O(1)  | `deque.popleft()` |
| Peek      | O(1) | O(1)  | `deque[0]` |
| Search    | O(N) | O(1)  | `val in queue` |

Best Practices:
- **Implementation**: Use `collections.deque`. Do NOT use `list` (pop(0) is O(N)).
- **FIFO**: First In, First Out.
- **BFS**: Queue is the standard structure for Breadth-First Search.
"""

from typing import Deque, Optional, Any, List
from collections import deque

class QueuePatterns:
    """
    Encapsulates common patterns and operations for Queues.
    """

    def initialization(self) -> Deque[int]:
        """
        Initialize an empty queue.
        """
        return deque()

    def enqueue(self, queue: Deque[Any], val: Any) -> None:
        """
        Add element to end of queue.
        
        Complexity: O(1)
        """
        queue.append(val)

    def dequeue(self, queue: Deque[Any]) -> Optional[Any]:
        """
        Remove element from front of queue.
        
        Complexity: O(1)
        """
        if not queue:
            return None
        return queue.popleft()

    def peek(self, queue: Deque[Any]) -> Optional[Any]:
        """
        Peek at front element.
        
        Complexity: O(1)
        """
        if not queue:
            return None
        return queue[0]

    def is_empty(self, queue: Deque[Any]) -> bool:
        """
        Check if queue is empty.
        
        Complexity: O(1)
        """
        return len(queue) == 0

    def moving_average(self, nums: List[int], window_size: int) -> List[float]:
        """
        Common Pattern: Sliding Window using Queue.
        
        Complexity: O(N)
        """
        queue = deque()
        result = []
        window_sum = 0
        
        for num in nums:
            queue.append(num)
            window_sum += num
            
            if len(queue) > window_size:
                removed = queue.popleft()
                window_sum -= removed
                
            result.append(window_sum / len(queue))
            
        return result

if __name__ == "__main__":
    solver = QueuePatterns()
    
    # 1. Basic Ops
    q = solver.initialization()
    solver.enqueue(q, 1)
    solver.enqueue(q, 2)
    front = solver.peek(q) # 1
    val = solver.dequeue(q) # 1
    
    # 2. Patterns
    avgs = solver.moving_average([1, 10, 3, 5], 3)
