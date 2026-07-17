# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head.next
            fast = head.next.next
        except:
            return False

        while slow:
            if slow == fast:
                return True
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return False
        
        return False