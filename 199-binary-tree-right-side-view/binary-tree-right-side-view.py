# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        max_level = -1

        def dfs(node,level):
            if not node :
                return 
            nonlocal max_level
            if level > max_level :
                res.append(node.val)
                max_level = level
            dfs(node.right,level+1)
            dfs(node.left, level+1)

        dfs(root,0)
        return res