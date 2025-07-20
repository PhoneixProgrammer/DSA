# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root :
            return False
        if self.isSameTree(root,subRoot):
            return True 
        #Recursively search in the left and right subtrees
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def isSameTree(self,s:TreeNode, t:TreeNode) -> bool :
        if not s and not t :
            return True 
        if not s or not t :
            return False
        if s.val != t.val :
            return False
        
        #Both values match, now check left and right subtrees
        return self.isSameTree(s.left,t.left) and self.isSameTree(s.right,t.right)