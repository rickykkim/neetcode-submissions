# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        start = len(nodes) - n - 1
        if start < 0:
            return head.next
        else:
            nodes[start].next = nodes[start].next.next
            return head
        