# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.check(root, float('-inf'), float('inf'))
        
    def check(self, root, min_val, max_val):
        if not root:
            return True
        
        if min_val < root.val < max_val:
            return self.check(root.left, min_val, root.val) \
            and self.check(root.right, root.val, max_val)
        else:
            return False