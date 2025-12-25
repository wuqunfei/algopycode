"""
Recursion & Backtracking Template
=================================

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Recursion | O(B^D)   | O(D)  | B=Branch factor, D=Depth |
| Backtracking| O(B^D) | O(D) | Pruning reduces effective search space |

Best Practices:
- **Base Case**: Stop condition is critical.
- **State**: Pass current state (index, current_path) in arguments.
- **Backtrack**: Add -> Recurse -> Remove (Undo change).
- **Memoization**: Cache results to convert Recursion -> DP.
"""

from typing import List

class RecursionTemplate:
    """
    Encapsulates high-level generic template for Recursion/Backtracking.
    """

    def solve(self, data: List[int]) -> List[List[int]]:
        """
        Generic Backtracking Template.
        """
        result = []
        
        def backtrack(path, options):
            # 1. Base Case: Goal reached
            if self._is_goal(path):
                result.append(path[:])
                return
            
            # 2. Iterate Choices
            for choice in options:
                if self._is_valid(choice, path):
                    # 3. Make Choice
                    path.append(choice)
                    
                    # 4. Recurse
                    backtrack(path, options)
                    
                    # 5. Undo Choice (Backtrack)
                    path.pop()
                    
        backtrack([], data)
        return result

    def _is_goal(self, path) -> bool: return False
    def _is_valid(self, choice, path) -> bool: return True


class RecursionExamples:
    """
    Concrete examples of Recursion patterns.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Concrete Example: Subsets (LeetCode 78).
        Generate all power sets.
        """
        result = []
        n = len(nums)
        
        def backtrack(start_index, current_subset):
            # Every state is a valid subset
            result.append(current_subset[:])
            
            for i in range(start_index, n):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(0, [])
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Concrete Example: Permutations (LeetCode 46).
        Generate all permutations.
        """
        result = []
        
        def backtrack(current_perm):
            if len(current_perm) == len(nums):
                result.append(current_perm[:])
                return
            
            for num in nums:
                if num not in current_perm: # Note: O(N) check, efficient for small N
                    current_perm.append(num)
                    backtrack(current_perm)
                    current_perm.pop()
                    
        backtrack([])
        return result

if __name__ == "__main__":
    # 2. Examples
    examples = RecursionExamples()
    
    # Subsets
    res_sub = examples.subsets([1, 2, 3])
    print(f"Example Result (Subsets): {res_sub}")
    
    # Permutations
    res_perm = examples.permute([1, 2, 3])
    print(f"Example Result (Permutations): {res_perm}")
