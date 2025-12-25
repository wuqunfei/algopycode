"""
Trie (Prefix Tree) Template
===========================

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Insert    | O(M) | O(M)  | M is length of word |
| Search    | O(M) | O(1)  | M is length of word |
| StartsWith| O(M) | O(1)  | Check prefix |

Best Practices:
- **Use Case**: Autocomplete, Spell Checker, Longest Common Prefix.
- **Structure**: Dictionary of dictionaries or custom Node class.
- **Space**: Can be space-heavy O(N*M), but optimizes prefix sharing.
"""

from typing import Dict, Optional

class TrieNode:
    """Definition for a Trie node."""
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class TriePatterns:
    """
    Encapsulates common patterns and operations for Trie.
    """

    def __init__(self):
        """
        Initialize Trie with a root node.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Complexity: O(M)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        
        Complexity: O(M)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        
        Complexity: O(M)
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    trie = TriePatterns()
    
    # 1. Insert
    trie.insert("apple")
    
    # 2. Search
    found_apple = trie.search("apple")   # True
    found_app = trie.search("app")       # False
    
    # 3. Prefix
    starts_app = trie.starts_with("app") # True
    starts_b = trie.starts_with("b")     # False
    
    trie.insert("app")
    found_app_after = trie.search("app") # True
