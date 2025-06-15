# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        result = []

        def dfs(node, path):
            if not node:
                return
            
            #append current node to path
            path = path +str(node.val)

            #If its a leaf, add the path to result
            if not node.left and not node.right :
                result.append(path)
            else:
                #otherwise,keep traversing
                path += "->"
                dfs(node.left,path)
                dfs(node.right,path)

        dfs(root,"")
        return result