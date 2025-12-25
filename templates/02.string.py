"""
String Data Structure Template
==============================

Complexity Summary (Average Case)
---------------------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access    | O(1) | O(1)  | Indexing (e.g., s[i]) |
| Search    | O(N) | O(1)  | Find substring/char (e.g., 'sub' in s) |
| Insertion | O(N) | O(N)  | Strings are immutable (New string created) |
| Deletion  | O(N) | O(N)  | Strings are immutable (New string created) |
| Slice     | O(K) | O(K)  | Copying K chars |
| Join      | O(N) | O(N)  | Efficient concatenation |

Best Practices:
- **Immutability**: Python strings are immutable. Any modification creates a new string.
- **Concatenation**: Avoid `s += char` in loops (O(N^2)). Use `list` of chars and `"".join()` (O(N)).
- **Slicing**: Powerful but creates copies. Be mindful of memory in recursion.
- **Checking**: Use `s.isalnum()`, `s.isdigit()`, `s.isalpha()` for validation.
"""

from typing import List, Optional, Any

class StringPatterns:
    """
    Encapsulates common patterns and operations for Python Strings.
    """

    def initialization(self) -> dict:
        """
        Demonstrates various ways to initialize and create strings.
        
        Complexity:
            Time: O(N)
            Space: O(N)
        """
        # 1. Literal
        s1 = "Hello"
        
        # 2. From List (Join) - Best Practice
        chars = ['H', 'e', 'l', 'l', 'o']
        s2 = "".join(chars)
        
        # 3. Formatted String (f-string)
        val = 123
        s3 = f"Value: {val}"
        
        # 4. Multiplication
        s4 = "a" * 5  # "aaaaa"

        return {
            "literal": s1,
            "joined": s2,
            "formatted": s3,
            "multiplied": s4
        }

    def access_char(self, s: str, index: int) -> Optional[str]:
        """
        Access character by index.
        
        Complexity:
            Time: O(1)
            Space: O(1)
        
        Args:
            s: Input string.
            index: Index to access.
        """
        if -len(s) <= index < len(s):
            return s[index]
        return None

    def search_substring(self, s: str, sub: str) -> int:
        """
        Find index of first occurrence of substring.
        
        Complexity:
            Time: O(N*M) worst case, typically optimized (Boyer-Moore-like).
            Space: O(1)
            
        Returns:
            Index if found, -1 otherwise.
        """
        return s.find(sub)

    def contains_substring(self, s: str, sub: str) -> bool:
        """
        Check if substring exists.
        
        Complexity:
            Time: O(N)
            Space: O(1)
        """
        return sub in s

    def insert_char(self, s: str, index: int, char: str) -> str:
        """
        Insert character at index (Simulated).
        
        Complexity:
            Time: O(N) - Must create new string.
            Space: O(N)
        
        Note:
            Expensive operation. If doing multiple inserts, convert to list first.
        """
        return s[:index] + char + s[index:]

    def delete_char(self, s: str, index: int) -> str:
        """
        Delete character at index (Simulated).
        
        Complexity:
            Time: O(N) - Must create new string.
            Space: O(N)
        """
        return s[:index] + s[index+1:]

    def replace_substring(self, s: str, old: str, new: str) -> str:
        """
        Replace occurrences of substring.
        
        Complexity:
            Time: O(N)
            Space: O(N)
        """
        return s.replace(old, new)

    def slice_string(self, s: str, start: int, end: int) -> str:
        """
        Get substring via slicing.
        
        Complexity:
            Time: O(K) where K is slice length.
            Space: O(K)
        """
        return s[start:end]

    def reverse_string(self, s: str) -> str:
        """
        Reverse a string.
        
        Complexity:
            Time: O(N)
            Space: O(N)
        """
        return s[::-1]

    def split_string(self, s: str, delimiter: str = " ") -> List[str]:
        """
        Split string into list of substrings.
        
        Complexity:
            Time: O(N)
            Space: O(N)
        """
        return s.split(delimiter)

    def join_strings(self, parts: List[str], delimiter: str = "") -> str:
        """
        Join list of strings into one.
        
        Complexity:
            Time: O(N) - where N is total characters.
            Space: O(N)
            
        Note:
            This is the standard way to build strings efficiently.
        """
        return delimiter.join(parts)

    def clean_string(self, s: str) -> str:
        """
        Common LeetCode pattern: Clean string (lowercase + remove non-alphanumeric).
        
        Complexity:
            Time: O(N)
            Space: O(N)
        """
        return "".join(c.lower() for c in s if c.isalnum())

    def is_palindrome(self, s: str) -> bool:
        """
        Check if string is palindrome (Two Pointers).
        
        Complexity:
            Time: O(N)
            Space: O(1) if checking indices, O(N) if cleaning first.
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solver = StringPatterns()
    
    # 1. Initialization
    init = solver.initialization()
    
    # 2. Access
    char = solver.access_char("Hello", 1)  # 'e'
    
    # 3. Search
    idx = solver.search_substring("Hello World", "World") # 6
    exists = solver.contains_substring("Hello", "ell")    # True
    
    # 4. Modification (Simulated)
    inserted = solver.insert_char("Hello", 5, "!")  # "Hello!"
    deleted = solver.delete_char("Hello", 1)        # "Hllo"
    replaced = solver.replace_substring("Hello", "l", "w") # "Hewwo"
    
    # 5. Slicing & Reversing
    sub = solver.slice_string("Hello", 0, 2) # "He"
    rev = solver.reverse_string("Hello")     # "olleH"
    
    # 6. Split & Join
    parts = solver.split_string("a,b,c", ",") # ['a', 'b', 'c']
    joined = solver.join_strings(parts, "-")  # "a-b-c"
    
    # 7. Common LeetCode Patterns
    cleaned = solver.clean_string("A man, a plan!") # "amanaplan"
    is_pal = solver.is_palindrome("racecar")        # True
