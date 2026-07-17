# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p or queue_q:
            node_p = queue_p.popleft()
            node_q = queue_q.popleft()

            if node_p is None or node_q is None:
                if node_p != node_q:
                    return False
            elif node_p.val != node_q.val:
                return False
            
            if node_p is not None:
                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
            if node_q is not None:
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)
        
        return True