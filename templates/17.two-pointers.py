"""
Two Pointers Template
=====================

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Linear Scan | O(N)   | O(1)  | Start from both ends or same end |
| Partition | O(N)     | O(1)  | QuickSort partition step |

Best Practices:
- **Sorted Input**: Often required (e.g., Two Sum II).
- **Direction**:
    - **Opposite**: Left -> <- Right (Searching, Palindrome).
    - **Same**: Slow -> Fast -> (Remove Duplicates, Cycle Detection).
"""

from typing import List

class TwoPointersTemplate:
    """
    Encapsulates high-level generic template for Two Pointers.
    """

    def solve_opposite(self, nums: List[int]) -> int:
        """
        Template for pointers moving towards each other.
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            # Check condition using nums[left] and nums[right]
            if self._condition(nums[left], nums[right]):
                return 1 # Found
            
            # Move pointers based on logic
            if True: 
                left += 1
            else:
                right -= 1
        return 0

    def _condition(self, val1: int, val2: int) -> bool:
        return False


class TwoPointersExamples:
    """
    Concrete examples of Two Pointers patterns.
    """

    def two_sum_sorted(self, numbers: List[int], target: int) -> List[int]:
        """
        Concrete Example: Two Sum II - Input Array Sorted (LeetCode 167).
        
        Pattern: Opposite Direction.
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            
            if curr_sum == target:
                return [left + 1, right + 1] # 1-based index
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return []

    def is_palindrome(self, s: str) -> bool:
        """
        Concrete Example: Valid Palindrome (LeetCode 125).
        
        Pattern: Opposite Direction with skipping.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
        return True

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Concrete Example: Remove Duplicates from Sorted Array (LeetCode 26).
        
        Pattern: Same Direction (Slow/Fast).
        """
        if not nums:
            return 0
            
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                
        return slow + 1

if __name__ == "__main__":
    # 2. Examples
    examples = TwoPointersExamples()
    
    # Two Sum Sorted
    res_sum = examples.two_sum_sorted([2, 7, 11, 15], 9)
    print(f"Example Result (Two Sum): {res_sum}") # [1, 2]
    
    # Palindrome
    res_pal = examples.is_palindrome("A man, a plan, a canal: Panama")
    print(f"Example Result (Palindrome): {res_pal}") # True
