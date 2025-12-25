"""
Bitmask Template
================

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Set Bit   | O(1) | O(1)  | `mask | (1 << i)` |
| Unset Bit | O(1) | O(1)  | `mask & ~(1 << i)` |
| Check Bit | O(1) | O(1)  | `mask & (1 << i)` |
| Toggle    | O(1) | O(1)  | `mask ^ (1 << i)` |
| Iterate Subsets | O(3^N) | O(1) | Iterate all submasks |

Best Practices:
- **Small N**: Typically N <= 20 due to 2^N complexity.
- **Sets**: Represents a set of elements efficiently.
- **DP**: Common state in DP (Bitmask DP).
"""

from typing import List

class BitmaskTemplate:
    """
    Encapsulates high-level generic template for Bitmasking.
    """

    def basic_ops(self):
        """
        Demonstrate basic bitwise operations.
        """
        mask = 0
        
        # Set 3rd bit (0-indexed)
        mask |= (1 << 3) # 1000 (8)
        
        # Check 3rd bit
        has_third = (mask & (1 << 3)) != 0
        
        # Toggle 3rd bit
        mask ^= (1 << 3) # 0000
        
        return has_third


class BitmaskExamples:
    """
    Concrete examples of Bitmask patterns.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Concrete Example: Subsets (LeetCode 78) using Bitmask.
        Generate 2^N subsets by iterating 0 to 2^N - 1.
        """
        n = len(nums)
        result = []
        
        # Iterate from 0 to 2^n - 1
        # Each number represents a subset
        for i in range(1 << n):
            subset = []
            for j in range(n):
                # Check if j-th bit is set
                if (i >> j) & 1:
                    subset.append(nums[j])
            result.append(subset)
            
        return result

if __name__ == "__main__":
    # 2. Examples
    examples = BitmaskExamples()
    
    # Subsets
    res_sub = examples.subsets([1, 2, 3])
    print(f"Example Result (Subsets via Bitmask): {res_sub}")
