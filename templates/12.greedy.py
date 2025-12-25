"""
Greedy Algorithm Template
=========================

Complexity Summary
------------------
| Operation | Time     | Space    | Notes |
|-----------|----------|----------|-------|
| Sorting   | O(N log N)| O(1)/O(N)| Often the first step in Greedy |
| Iteration | O(N)     | O(1)     | One pass to make local optimal choices |
| Heap Ops  | O(N log N)| O(N)     | Priority Queue for dynamic selection |

Best Practices:
- **Local Optimum**: Make the best choice at the current step.
- **Sorting**: Often required to structure the problem (e.g., by end time, by cost).
- **Feasibility**: Check if the local choice satisfies constraints.
- **Proof**: Ensure local optimal leads to global optimal (unlike DP).
"""

from typing import List

class GreedyTemplate:
    """
    Encapsulates high-level generic template for Greedy Algorithms.
    """

    def solve(self, data: List[int]) -> int:
        """
        A high-level view of the Greedy Algorithm structure.
        
        Steps:
        1. Pre-process (often Sorting or Heapify)
        2. Initialize Result/State
        3. Iterate and make greedy choice
        4. Update Result if choice is feasible
        """
        n = len(data)
        if n == 0:
            return 0
            
        # 1. Pre-process
        # Sorting is common to enable greedy choices
        data.sort() 
        # or data.sort(reverse=True)
        
        # 2. Initialize Result
        result = 0
        
        # 3. Iterate
        for i in range(n):
            current_choice = data[i]
            
            # Check feasibility / Greedy Condition
            if self._is_feasible(current_choice):
                # 4. Make Greedy Choice
                result = self._apply_choice(result, current_choice)
                
        return result

    def _is_feasible(self, choice: int) -> bool:
        """
        Check if the current choice is valid under constraints.
        """
        return True # Placeholder

    def _apply_choice(self, current_result: int, choice: int) -> int:
        """
        Update the result with the chosen greedy option.
        """
        return current_result + 1 # Placeholder


class GreedyExamples:
    """
    Concrete examples of Greedy patterns.
    """

    def assign_cookies(self, g: List[int], s: List[int]) -> int:
        """
        Concrete Example: Assign Cookies (LeetCode 455).
        Problem: You have children with greed factors `g` and cookies with sizes `s`.
        Maximize the number of content children. Each child gets at most one cookie.
        
        Strategy:
        - Sort both greed factors and cookie sizes.
        - Give the smallest cookie that satisfies the least greedy child.
        """
        # 1. Pre-process (Sort)
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_j = 0
        content_children = 0
        
        # 2. Iterate
        while child_i < len(g) and cookie_j < len(s):
            # Greedy Condition: Does this cookie satisfy this child?
            if s[cookie_j] >= g[child_i]:
                # 3. Make Choice
                content_children += 1
                child_i += 1 # Move to next child
            
            # Move to next cookie regardless (used or too small)
            cookie_j += 1
            
        return content_children

if __name__ == "__main__":
    # 1. Use Generic Template
    template_solver = GreedyTemplate()
    # Example: Simple Count
    res_template = template_solver.solve([1, 2, 3])
    print(f"Template Result: {res_template}")
    
    # 2. Use Concrete Pattern
    pattern_solver = GreedyExamples()
    # Example: Assign Cookies
    # g=[1,2,3], s=[1,1] -> 1 child satisfied (child with greed 1 gets cookie 1)
    res_cookies = pattern_solver.assign_cookies([1, 2, 3], [1, 1])
    print(f"Pattern Result (Assign Cookies): {res_cookies}")
