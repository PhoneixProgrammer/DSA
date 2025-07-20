# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,low= float('-inf'),high=float('inf')):
            if not node:
                return True
            
            if not (low < node.val < high) :
                return False

            #Left subtree : all nodes < current node's value
            #Right subtree :  all nodes > current node's value
            return (validate(node.left,low,node.val) and validate(node.right,node.val,high))
        return validate(root)

        #time complexity : O(n) --> visit each node exactly once
        #space complexity : O(h) --> h  is height of the tree
        # balanced tree :O(logn )
        # skewed tree : O(n)