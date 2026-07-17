# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        ino_root_idx = inorder.index(preorder[0])
        
        left_ino = inorder[:ino_root_idx]
        right_ino = inorder[ino_root_idx+1:]
        left_preo = preorder[1:len(left_ino)+1]
        right_preo = preorder[len(left_ino)+1:]
        
        root.left = self.buildTree(left_preo, left_ino)
        root.right = self.buildTree(right_preo, right_ino)

        return root