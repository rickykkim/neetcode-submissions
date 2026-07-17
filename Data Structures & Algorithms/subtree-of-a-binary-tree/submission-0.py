# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot:
            return True
        if not root:
            return False
        
        if self.checkSub(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkSub(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot
        
        if root.val == subRoot.val:
            return self.checkSub(root.left, subRoot.left) and self.checkSub(root.right, subRoot.right)
        else:
            return False
        