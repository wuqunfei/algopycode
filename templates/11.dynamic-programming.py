"""
Dynamic Programming Template
============================

Complexity Summary
------------------
| Operation | Time     | Space    | Notes |
|-----------|----------|----------|-------|
| 1D DP     | O(N)     | O(N)     | Linear problems (e.g., Climbing Stairs) |
| 2D DP     | O(N*M)   | O(N*M)   | Grid/Sequence alignment problems |
| Space Opt | O(N)     | O(1)     | Rolling array (Fibonacci) |

Best Practices:
- **State Definition**: Clearly define what `dp[i]` represents.
- **Base Case**: Initialize starting values (e.g., `dp[0]`).
- **Transition**: The core recurrence relation `dp[i] = f(dp[i-1], ...)`.
- **Order**: Iteration direction (bottom-up vs top-down).
"""

from typing import List

class DynamicProgrammingTemplate:
    """
    Encapsulates high-level generic template for Dynamic Programming.
    """

    def solve(self, data: List[int]) -> int:
        """
        A high-level view of the 1D Dynamic Programming structure.
        
        Steps:
        1. Define State Array
        2. Initialize Base Cases
        3. Iterate through subproblems
        4. Apply Transition Equation
        """
        n = len(data)
        if n == 0:
            return 0
            
        # 1. Create State Array
        # dp[i] represents the optimal state at index i
        dp = [0] * n 
        
        # 2. Base Case (Init value)
        # Initialize the first element(s) based on problem constraints
        dp[0] = data[0] 
        
        # 3. Iterate (Direction: left -> right)
        for i in range(1, n):
            # Check boundaries and conditions
            if True: # Replace with actual condition if needed
                # 4. Transition Equation
                # Compute current state from previous states
                dp[i] = self._transition(dp[i - 1], data[i])
        
        # 5. Return Answer
        return dp[-1]

    def _transition(self, prev_state: int, current_val: int) -> int:
        """
        Helper to represent the core state change logic.
        Example: Summing up values (Prefix Sum).
        """
        return prev_state + current_val


class DynamicProgrammingExamples:
    """
    Concrete examples of Dynamic Programming patterns.
    """

    def climbing_stairs(self, n: int) -> int:
        """
        Concrete Simple Example: Climbing Stairs.
        Problem: You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. How many distinct ways can you climb to the top?
        
        Mapping to Template:
        - State: dp[i] = Number of ways to reach step i.
        - Base Case: dp[0]=1 (ground), dp[1]=1 (1st step).
        - Transition: dp[i] = dp[i-1] + dp[i-2] (Coming from 1 step below or 2 steps below).
        """
        if n <= 1:
            return 1
            
        # 1. Create State Array
        # Size is n + 1 because we include step 0 to step n
        dp = [0] * (n + 1)
        
        # 2. Base Cases
        dp[0] = 1
        dp[1] = 1
        
        # 3. Iterate
        for i in range(2, n + 1):
            # 4. Transition Equation
            dp[i] = dp[i - 1] + dp[i - 2]
            
        # 5. Return Answer
        return dp[n]

if __name__ == "__main__":
    # 1. Use Generic Template
    template_solver = DynamicProgrammingTemplate()
    # Example: High Level Template (Simulating Prefix Sum)
    # data: [1, 2, 3, 4] -> dp: [1, 3, 6, 10]
    result_template = template_solver.solve([1, 2, 3, 4]) # Returns 10
    print(f"Template Result (Prefix Sum): {result_template}")
    
    # 2. Use Concrete Pattern
    pattern_solver = DynamicProgrammingExamples()
    # Example: Climbing Stairs
    # n=5 -> 8 ways (1, 2, 3, 5, 8...)
    result_stairs = pattern_solver.climbing_stairs(5) # Returns 8
    print(f"Pattern Result (Climbing Stairs): {result_stairs}")
