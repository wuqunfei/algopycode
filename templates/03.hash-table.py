"""
Hash Table (Dictionary) Template
================================

Complexity Summary (Average Case)
---------------------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access    | O(1) | O(1)  | Get value by key |
| Search    | O(1) | O(1)  | Check key existence |
| Insertion | O(1) | O(1)  | Add new key-value |
| Deletion  | O(1) | O(1)  | Remove key |
| Iterate   | O(N) | O(N)  | Iterate over all keys |

Best Practices:
- **Lookups**: Use for O(1) access to data.
- **Counting**: Use `collections.Counter` for frequency counting.
- **Grouping**: Use `collections.defaultdict(list)` for grouping items.
- **Keys**: Must be immutable (int, string, tuple).
"""

from typing import Dict, List, Any, Optional
from collections import defaultdict, Counter

class HashTablePatterns:
    """
    Encapsulates common patterns and operations for Python Dictionaries (Hash Tables).
    """

    def initialization(self) -> dict:
        """
        Demonstrates various ways to initialize hash tables.
        """
        # 1. Literal
        d1 = {"a": 1, "b": 2}
        
        # 2. Dict constructor
        d2 = dict(a=1, b=2)
        
        # 3. List of tuples
        d3 = dict([("a", 1), ("b", 2)])
        
        # 4. Defaultdict (Best for grouping)
        d4 = defaultdict(list)
        
        # 5. Counter (Best for counting)
        d5 = Counter("hello")
        
        return {"literal": d1, "defaultdict": d4, "counter": d5}

    def insert_or_update(self, d: Dict[Any, Any], key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair.
        
        Complexity: O(1)
        """
        d[key] = value

    def get_value(self, d: Dict[Any, Any], key: Any) -> Optional[Any]:
        """
        Get value safely.
        
        Complexity: O(1)
        """
        return d.get(key)

    def check_existence(self, d: Dict[Any, Any], key: Any) -> bool:
        """
        Check if key exists.
        
        Complexity: O(1)
        """
        return key in d

    def remove_key(self, d: Dict[Any, Any], key: Any) -> None:
        """
        Remove key if it exists.
        
        Complexity: O(1)
        """
        if key in d:
            del d[key]
            # or d.pop(key)

    def iterate_items(self, d: Dict[Any, Any]) -> List[tuple]:
        """
        Iterate over key-value pairs.
        
        Complexity: O(N)
        """
        items = []
        for k, v in d.items():
            items.append((k, v))
        return items

    def count_frequencies(self, nums: List[int]) -> Dict[int, int]:
        """
        Count frequency of elements (Common LeetCode Pattern).
        
        Complexity: O(N)
        """
        # Manual
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        # Or simply: return Counter(nums)
        return counts

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group strings by sorted signature (Common LeetCode Pattern).
        
        Complexity: O(N * K * log K) where K is max string length.
        """
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s)) # Tuple is immutable/hashable
            groups[key].append(s)
        return list(groups.values())

if __name__ == "__main__":
    solver = HashTablePatterns()
    
    # 1. Init
    inits = solver.initialization()
    
    # 2. Basic Ops
    my_dict = {}
    solver.insert_or_update(my_dict, "name", "Alice")
    val = solver.get_value(my_dict, "name")
    exists = solver.check_existence(my_dict, "age")
    solver.remove_key(my_dict, "name")
    
    # 3. Patterns
    freqs = solver.count_frequencies([1, 1, 2, 3, 3, 3])
    anagrams = solver.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
