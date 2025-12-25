"""
Sliding Window Template
=======================

Complexity Summary
------------------
| Operation | Time     | Space | Notes |
|-----------|----------|-------|-------|
| Fixed Window | O(N) | O(1) | Subarrays of size K |
| Variable Window | O(N) | O(1)/O(K) | Longest/Shortest subarray satisfying condition |

Best Practices:
- **Expansion**: Right pointer moves to expand window.
- **Contraction**: Left pointer moves to shrink window (optimize/validate).
- **State**: Track window state (sum, count, etc.) incrementally.
"""

from typing import List, Dict
from collections import Counter

class SlidingWindowTemplate:
    """
    Encapsulates high-level generic template for Sliding Window.
    """

    def solve(self, s: str) -> int:
        """
        Generic Sliding Window Template.
        
        Steps:
        1. Initialize Pointers (left, right)
        2. Expand Right
        3. Update State
        4. Shrink Left (while invalid or to optimize)
        5. Update Result
        """
        left = 0
        result = 0
        state = {}
        
        for right in range(len(s)):
            # 1. Add current element to state
            char = s[right]
            self._add(state, char)
            
            # 2. Shrink window if condition is met/broken
            while self._should_shrink(state):
                left_char = s[left]
                self._remove(state, left_char)
                left += 1
                
            # 3. Update Result
            result = max(result, right - left + 1)
            
        return result

    def _add(self, state, val): pass
    def _remove(self, state, val): pass
    def _should_shrink(self, state) -> bool: return False


class SlidingWindowExamples:
    """
    Concrete examples of Sliding Window patterns.
    """

    def length_of_longest_substring(self, s: str) -> int:
        """
        Concrete Example: Longest Substring Without Repeating Characters (LeetCode 3).
        
        Pattern: Variable Window.
        """
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If char in window, move left past duplicate
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            char_map[char] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len

    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        """
        Concrete Example: Minimum Size Subarray Sum (LeetCode 209).
        
        Pattern: Variable Window (Shrink to find min).
        """
        left = 0
        current_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_len if min_len != float('inf') else 0

if __name__ == "__main__":
    # 2. Examples
    examples = SlidingWindowExamples()
    
    # Longest Substring
    res_long = examples.length_of_longest_substring("abcabcbb")
    print(f"Example Result (Longest Substring): {res_long}") # 3
    
    # Min Subarray
    res_min = examples.min_sub_array_len(7, [2,3,1,2,4,3])
    print(f"Example Result (Min Subarray): {res_min}") # 2
