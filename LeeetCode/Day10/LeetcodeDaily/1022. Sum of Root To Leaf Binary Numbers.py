# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,val):
        if (not root):
            return 0
        val=(2*val)+root.val   
        if not root.right and not root.right:
            return val 
        return self.solve(root.left,val)+self.solve(root.right,val) 
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.solve(root,0)
        