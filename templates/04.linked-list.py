"""
Linked List Template
====================

Complexity Summary
------------------
| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access    | O(N) | O(1)  | Must traverse from head |
| Search    | O(N) | O(1)  | Find value |
| Insertion | O(1) | O(1)  | If pointer is known (e.g., at head) |
| Deletion  | O(1) | O(1)  | If pointer is known (need prev node) |

Best Practices:
- **Dummy Head**: Use a dummy head node to simplify edge cases (insert/delete at head).
- **Two Pointers**: Use Fast & Slow pointers for cycle detection or finding middle.
- **Reverse**: Know how to reverse iteratively and recursively.
"""

from typing import Optional, List

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListPatterns:
    """
    Encapsulates common patterns and operations for Linked Lists.
    """

    def create_linked_list(self, values: List[int]) -> Optional[ListNode]:
        """
        Helper to create a linked list from a list of values.
        
        Complexity: O(N)
        """
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def get_node(self, head: Optional[ListNode], index: int) -> Optional[ListNode]:
        """
        Get node at specific index (0-based).
        
        Complexity: O(N)
        """
        curr = head
        for _ in range(index):
            if not curr:
                return None
            curr = curr.next
        return curr

    def insert_at_head(self, head: Optional[ListNode], val: int) -> ListNode:
        """
        Insert new node at the beginning.
        
        Complexity: O(1)
        """
        new_node = ListNode(val)
        new_node.next = head
        return new_node

    def insert_after(self, prev_node: ListNode, val: int) -> None:
        """
        Insert new node after a given node.
        
        Complexity: O(1)
        """
        if not prev_node:
            return
        new_node = ListNode(val)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Delete first occurrence of value.
        
        Complexity: O(N)
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                return dummy.next
            prev = curr
            curr = curr.next
            
        return dummy.next

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.
        
        Complexity: O(N)
        """
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node using Slow & Fast pointers.
        
        Complexity: O(N)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect cycle using Floyd's Cycle-Finding Algorithm.
        
        Complexity: O(N)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    solver = LinkedListPatterns()
    
    # 1. Create
    head = solver.create_linked_list([1, 2, 3, 4, 5])
    
    # 2. Insert
    head = solver.insert_at_head(head, 0) # 0->1->2->3->4->5
    
    # 3. Access
    node = solver.get_node(head, 2) # Node(2)
    
    # 4. Reverse
    rev_head = solver.reverse_list(head) # 5->4->3->2->1->0
    
    # 5. Middle
    mid = solver.middle_node(rev_head) # Node(2)
