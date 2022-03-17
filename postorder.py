# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.postorder(root)
        return self.arr
        
    def postorder(self,node):
        if(node!=None):
            self.postorder(node.left)
            self.postorder(node.right)
            self.arr.append(node.val)
        else:
            return
    
            
