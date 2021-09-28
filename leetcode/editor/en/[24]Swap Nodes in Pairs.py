# Given a linked list, swap every two adjacent nodes and return its head. You 
# must solve the problem without modifying the values in the list's nodes (i.e., 
# only nodes themselves may be changed.) 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 100]. 
#  0 <= Node.val <= 100 
#  
#  Related Topics Linked List Recursion 👍 4600 👎 243


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        """
        set nodes
        """
        curr_node = head
        next_node = head.next

        """
        swapping
        """
        curr_node.next = self.swapPairs(next_node.next)
        next_node.next = curr_node
        return next_node

# leetcode submit region end(Prohibit modification and deletion)
