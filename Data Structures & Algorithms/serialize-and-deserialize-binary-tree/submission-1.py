# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = ""
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                output += str(curr.val) + ","
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                output += "N,"
        return output[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "N":
            return None
            
        tree_list = data.split(",")
        root = TreeNode(int(tree_list[0]))
        queue = deque([root])
        idx = 1
        while queue and idx < len(tree_list):
            curr = queue.popleft()
            if tree_list[idx] != "N":
                node = TreeNode(int(tree_list[idx]))
                curr.left = node
                queue.append(node)
            idx += 1
            if tree_list[idx] != "N":
                node = TreeNode(int(tree_list[idx]))
                curr.right = node
                queue.append(node)
            idx += 1
        return root