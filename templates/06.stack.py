"""
Stack Template
==============

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Push      | O(1) | O(1)  | `list.append()` |
| Pop       | O(1) | O(1)  | `list.pop()` (from end) |
| Peek      | O(1) | O(1)  | `list[-1]` |
| Search    | O(N) | O(1)  | `val in stack` |

Best Practices:
- **Implementation**: Use Python's built-in `list`.
- **LIFO**: Last In, First Out.
- **Monotonic Stack**: Powerful for "Next Greater Element" problems.
- **Recursion**: Stack simulates recursion (DFS).
"""

from typing import List, Optional, Any

class StackPatterns:
    """
    Encapsulates common patterns and operations for Stacks.
    """

    def initialization(self) -> List[int]:
        """
        Initialize an empty stack.
        """
        return []

    def push(self, stack: List[Any], val: Any) -> None:
        """
        Push element onto stack.
        
        Complexity: O(1)
        """
        stack.append(val)

    def pop(self, stack: List[Any]) -> Optional[Any]:
        """
        Pop element from stack.
        
        Complexity: O(1)
        """
        if not stack:
            return None
        return stack.pop()

    def peek(self, stack: List[Any]) -> Optional[Any]:
        """
        Peek at top element without removing.
        
        Complexity: O(1)
        """
        if not stack:
            return None
        return stack[-1]

    def is_empty(self, stack: List[Any]) -> bool:
        """
        Check if stack is empty.
        
        Complexity: O(1)
        """
        return len(stack) == 0

    def valid_parentheses(self, s: str) -> bool:
        """
        Common Pattern: Check valid parentheses.
        
        Complexity: O(N)
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # Opening bracket
                stack.append(char)
        
        return not stack

    def next_greater_element(self, nums: List[int]) -> List[int]:
        """
        Common Pattern: Monotonic Stack (Decreasing).
        Find next greater element for each element.
        
        Complexity: O(N)
        """
        res = [-1] * len(nums)
        stack = [] # Stores indices
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = num
            stack.append(i)
            
        return res

if __name__ == "__main__":
    solver = StackPatterns()
    
    # 1. Basic Ops
    stack = solver.initialization()
    solver.push(stack, 10)
    solver.push(stack, 20)
    top = solver.peek(stack) # 20
    popped = solver.pop(stack) # 20
    
    # 2. Patterns
    is_valid = solver.valid_parentheses("()[]{}") # True
    nge = solver.next_greater_element([2, 1, 2, 4, 3]) # [4, 2, 4, -1, -1]
