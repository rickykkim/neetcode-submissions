# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        curr = head

        while curr:
            unreversed = curr.next
            curr.next = reverse
            reverse = curr
            curr = unreversed
        
        return reverse