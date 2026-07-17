# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        current = head

        while current:
            original = current.next
            current.next = reverse
            reverse = current
            current = original
        
        return reverse