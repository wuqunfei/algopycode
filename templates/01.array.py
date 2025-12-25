"""
Array (List) Data Structure Template
====================================

Complexity Summary (Average Case)
---------------------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access    | O(1) | O(1)  | Indexing (e.g., arr[i]) |
| Search    | O(N) | O(1)  | Linear Scan (e.g., val in arr) |
| Insertion | O(N) | O(1)  | Insert at index (Amortized O(1) at end) |
| Deletion  | O(N) | O(1)  | Remove middle/start (O(1) at end) |

Best Practices:
- Use Arrays (Lists) for ordered collections where index access is frequent.
- For Queue (FIFO) behavior, prefer `collections.deque` over `list.pop(0)`.
- For frequent membership checks, convert to Set (O(1) search).
- Avoid string concatenation in loops; use `"".join(list_of_strings)`.
"""

from typing import List, Optional, Any, Union

class ArrayPatterns:
    """
    Encapsulates common patterns and operations for Python Lists (Arrays).
    """

    def initialization(self) -> dict:
        """
        Demonstrates various ways to initialize arrays.
        """
        # 1. Basic initialization
        nums = [1, 2, 3, 4, 5]

        # 2. Fixed size array (e.g., for frequency map or DP)
        # Time: O(N)
        zeros = [0] * 10

        # 3. 2D Array (Matrix) - Correct way to avoid shared references
        # Time: O(Rows * Cols)
        rows, cols = 3, 4
        matrix = [[0] * cols for _ in range(rows)]
        
        # 4. Generator Expression
        squares = list(x**2 for x in range(5))

        return {
            "nums": nums, 
            "zeros": zeros, 
            "matrix": matrix, 
            "squares": squares
        }

    def access_element(self, nums: List[Any], index: int) -> Optional[Any]:
        """
        Access element by index.
        Time: O(1)
        """
        if -len(nums) <= index < len(nums):
            return nums[index]
        return None

    def search_element(self, nums: List[Any], value: Any) -> int:
        """
        Search for an element and return its index.
        Time: O(N)
        """
        try:
            return nums.index(value)
        except ValueError:
            return -1

    def insert_element(self, nums: List[Any], index: int, value: Any) -> None:
        """
        Insert element at specific index.
        Time: O(N) because elements shift.
        """
        nums.insert(index, value)

    def append_element(self, nums: List[Any], value: Any) -> None:
        """
        Add element to the end.
        Time: O(1) Amortized.
        """
        nums.append(value)

    def delete_by_index(self, nums: List[Any], index: int) -> Optional[Any]:
        """
        Remove element at specific index.
        Time: O(N) because elements shift.
        """
        if -len(nums) <= index < len(nums):
            return nums.pop(index)
        return None

    def delete_by_value(self, nums: List[Any], value: Any) -> bool:
        """
        Remove first occurrence of a value.
        Time: O(N).
        """
        try:
            nums.remove(value)
            return True
        except ValueError:
            return False

    def slice_array(self, nums: List[Any], start: int, end: int, step: int = 1) -> List[Any]:
        """
        Create a shallow copy of a subarray.
        Time: O(K) where K is slice length.
        """
        return nums[start:end:step]

    def sort_array(self, nums: List[Any], reverse: bool = False) -> None:
        """
        Sort the array in-place.
        Time: O(N log N) (Timsort).
        """
        nums.sort(reverse=reverse)

    def reverse_array(self, nums: List[Any]) -> None:
        """
        Reverse the array in-place.
        Time: O(N).
        """
        nums.reverse()

if __name__ == "__main__":
    # Example usage (No print statements as requested)
    solver = ArrayPatterns()
    
    # 1. Initialization
    init_data = solver.initialization()
    my_list = [10, 20, 30, 40, 50]

    # 2. Access
    val = solver.access_element(my_list, 2)  # 30

    # 3. Search
    idx = solver.search_element(my_list, 40) # 3

    # 4. Insert
    solver.insert_element(my_list, 1, 15)    # [10, 15, 20, 30, 40, 50]

    # 5. Append
    solver.append_element(my_list, 60)       # [10, 15, 20, 30, 40, 50, 60]

    # 6. Delete
    popped = solver.delete_by_index(my_list, 0) # 10 removed
    removed = solver.delete_by_value(my_list, 50) # True

    # 7. Slicing
    sub = solver.slice_array(my_list, 0, 3)

    # 8. Sorting & Reversing
    solver.reverse_array(my_list)
    solver.sort_array(my_list)
