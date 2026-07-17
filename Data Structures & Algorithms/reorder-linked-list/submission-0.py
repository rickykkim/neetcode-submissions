# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next
        
        max_idx = int(len(nodes)//2)

        for i in range(max_idx):
            nodes[i].next = nodes[-i-1]

            if i == max_idx - 1 and len(nodes) % 2 == 1:
                # do one more forward
                nodes[-i-1].next = nodes[i+1]
                nodes[i+1].next = None
            elif i == max_idx - 1:
                nodes[-i-1].next = None
            else:
                nodes[-i-1].next = nodes[i+1]