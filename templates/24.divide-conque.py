"""
Divide and Conquer Template
===========================

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Merge Sort| O(N log N) | O(N) | Split, Sort, Merge |
| Quick Sort| O(N log N) | O(log N) | Partition, Sort |
| Binary Search | O(log N) | O(1) | Discard half |

Best Practices:
- **Structure**: Divide (split problem), Conquer (solve subproblems), Combine (merge results).
- **Base Case**: Essential to stop recursion.
- **Master Theorem**: Used to analyze complexity.
"""

from typing import List, Optional

class DivideConquerTemplate:
    """
    Encapsulates high-level generic template for Divide and Conquer.
    """

    def solve(self, problem):
        """
        Generic D&C Template.
        """
        # 1. Base Case
        if self._is_base_case(problem):
            return self._solve_base(problem)
            
        # 2. Divide
        subproblems = self._divide(problem)
        
        # 3. Conquer
        results = [self.solve(sub) for sub in subproblems]
        
        # 4. Combine
        return self._combine(results)

    def _is_base_case(self, p): return False
    def _solve_base(self, p): return None
    def _divide(self, p): return []
    def _combine(self, res): return None


class DivideConquerExamples:
    """
    Concrete examples of Divide and Conquer patterns.
    """

    def majority_element(self, nums: List[int]) -> int:
        """
        Concrete Example: Majority Element (LeetCode 169).
        Using Divide and Conquer.
        """
        def solve_dc(lo, hi):
            # Base case: single element
            if lo == hi:
                return nums[lo]
            
            mid = (hi - lo) // 2 + lo
            left = solve_dc(lo, mid)
            right = solve_dc(mid + 1, hi)
            
            if left == right:
                return left
            
            # Combine: count frequency
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)
            
            return left if left_count > right_count else right
            
        return solve_dc(0, len(nums) - 1)

    def max_sub_array(self, nums: List[int]) -> int:
        """
        Concrete Example: Maximum Subarray (LeetCode 53).
        Using Divide and Conquer (though Kadane's is O(N)).
        """
        def solve_dc(lo, hi):
            if lo == hi:
                return nums[lo]
            
            mid = (lo + hi) // 2
            
            left_sum = solve_dc(lo, mid)
            right_sum = solve_dc(mid + 1, hi)
            cross_sum = cross_max(lo, mid, hi)
            
            return max(left_sum, right_sum, cross_sum)
            
        def cross_max(lo, mid, hi):
            left_part = float('-inf')
            curr = 0
            for i in range(mid, lo - 1, -1):
                curr += nums[i]
                left_part = max(left_part, curr)
                
            right_part = float('-inf')
            curr = 0
            for i in range(mid + 1, hi + 1):
                curr += nums[i]
                right_part = max(right_part, curr)
                
            return left_part + right_part
            
        return solve_dc(0, len(nums) - 1)

if __name__ == "__main__":
    # 2. Examples
    examples = DivideConquerExamples()
    
    # Majority Element
    res_maj = examples.majority_element([2,2,1,1,1,2,2])
    print(f"Example Result (Majority): {res_maj}") # 2
    
    # Max Subarray
    res_max = examples.max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    print(f"Example Result (Max Subarray): {res_max}") # 6
