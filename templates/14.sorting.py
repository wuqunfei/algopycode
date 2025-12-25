"""
Sorting Template
================

Complexity Summary
------------------
| Algorithm | Time (Avg)| Time (Worst)| Space | Stability |
|-----------|-----------|-------------|-------|-----------|
| Quick Sort| O(N log N)| O(N^2)      | O(log N)| No      |
| Merge Sort| O(N log N)| O(N log N)  | O(N)  | Yes       |
| Heap Sort | O(N log N)| O(N log N)  | O(1)  | No        |

Best Practices:
- **Built-in**: Python's `sort()` (Timsort) is O(N log N) and stable. Use it by default.
- **Custom Sort**: Use `key` parameter in `sort()` for custom comparators.
- **Divide & Conquer**: Merge Sort is a classic D&C example.
"""

from typing import List

class SortingTemplate:
    """
    Encapsulates high-level generic template for Sorting.
    """

    def solve(self, nums: List[int]) -> List[int]:
        """
        High-level wrapper for sorting.
        """
        # Python's built-in sort is highly optimized (Timsort)
        nums.sort()
        return nums

    def merge_sort_template(self, nums: List[int]) -> List[int]:
        """
        Classic Merge Sort Implementation (Divide & Conquer).
        
        Steps:
        1. Base Case (len <= 1)
        2. Split into halves
        3. Recursively sort halves
        4. Merge sorted halves
        """
        if len(nums) <= 1:
            return nums
            
        mid = len(nums) // 2
        left = self.merge_sort_template(nums[:mid])
        right = self.merge_sort_template(nums[mid:])
        
        return self._merge(left, right)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """
        Merge two sorted lists.
        """
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


class SortingExamples:
    """
    Concrete examples of Sorting patterns.
    """

    def sort_colors(self, nums: List[int]) -> None:
        """
        Concrete Example: Sort Colors (LeetCode 75) - Dutch National Flag.
        Sort array of 0s, 1s, and 2s in one pass (O(N)) and O(1) space.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

if __name__ == "__main__":
    # 1. Template
    template = SortingTemplate()
    res_merge = template.merge_sort_template([38, 27, 43, 3, 9, 82, 10])
    print(f"Template Result (Merge Sort): {res_merge}")
    
    # 2. Examples
    examples = SortingExamples()
    colors = [2, 0, 2, 1, 1, 0]
    examples.sort_colors(colors)
    print(f"Example Result (Sort Colors): {colors}")
