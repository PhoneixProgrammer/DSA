# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case : if the tree is empty 
        if root is None :
            return 0

        #Recursively compute the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        #Depth of the current node is 1+  the max of left and right depths
        return 1 + max(left_depth,right_depth)

        #Time Complexity : O(n)
        #Space Complexity : O(h)