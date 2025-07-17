# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Both nodes are none
        if not p and not q :
            return True
        
        #One is Nonce, the other isn't 
        if not p or not q :
            return False

        #Current nodes value differe
        if p.val != q.val:
            return False

        #recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)

        #time complexity : O(n)
        #space complexity : O(h)--> due to recursion stack (height of tree)
