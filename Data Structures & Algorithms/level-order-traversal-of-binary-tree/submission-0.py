# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        current = 0
        full = []
        sub = []
        idx_queue = [0]
        queue = deque([root])

        while queue:
            node = queue.popleft()
            idx = idx_queue.pop(0)

            if idx > current:
                full.append(sub)
                current += 1
                sub = []
            
            sub.append(node.val)

            if node.left:
                queue.append(node.left)
                idx_queue.append(current + 1)
            if node.right:
                queue.append(node.right)
                idx_queue.append(current + 1)
        
        full.append(sub)
        return full