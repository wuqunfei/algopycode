"""
Binary Search Template
======================

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Search    | O(log N) | O(1)  | Input must be sorted |
| Lower/Upper Bound | O(log N) | O(1) | Find insertion point |

Best Practices:
- **Sorted Input**: Essential precondition.
- **Mid Calculation**: `mid = left + (right - left) // 2` prevents overflow.
- **Boundaries**: Careful with `left < right` vs `left <= right`.
- **Exit Condition**: Ensure loop terminates (avoid infinite loops).
"""

from typing import List

class BinarySearchTemplate:
    """
    Encapsulates high-level generic template for Binary Search.
    """

    def solve(self, nums: List[int], target: int) -> int:
        """
        Standard Binary Search Template.
        
        Steps:
        1. Define Search Space [left, right]
        2. Loop while space is valid
        3. Calculate mid
        4. Compare mid with target
        5. Adjust boundaries
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if self._check(nums[mid], target):
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

    def _check(self, current_val: int, target: int) -> bool:
        """
        Check condition (equality).
        """
        return current_val == target


class BinarySearchExamples:
    """
    Concrete examples of Binary Search patterns.
    """

    def search_insert_position(self, nums: List[int], target: int) -> int:
        """
        Concrete Example: Search Insert Position (LeetCode 35).
        Find index where target is found, or where it should be inserted.
        
        Pattern: Lower Bound.
        """
        left, right = 0, len(nums) # Note: right is len(nums) for insertion
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        return left

    def first_bad_version(self, n: int, bad_version: int) -> int:
        """
        Concrete Example: First Bad Version (LeetCode 278).
        Find the first element satisfying a condition (isBadVersion).
        
        Pattern: Minimize k such that condition(k) is True.
        """
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            if mid >= bad_version: # Simulated isBadVersion API
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    # 1. Template
    template = BinarySearchTemplate()
    res_bs = template.solve([-1, 0, 3, 5, 9, 12], 9)
    print(f"Template Result: {res_bs}") # 4
    
    # 2. Examples
    examples = BinarySearchExamples()
    res_insert = examples.search_insert_position([1, 3, 5, 6], 2)
    print(f"Example Result (Insert Pos): {res_insert}") # 1
