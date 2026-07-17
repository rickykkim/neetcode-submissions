# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = 0
        stack = []
        current = root

        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop(-1)
            visited += 1
            if visited == k:
                return current.val
            current = current.right