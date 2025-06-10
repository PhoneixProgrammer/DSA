# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        # Recursive solution
        result = []
        def dfs(node):
            if not node :
                return 
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result
        '''
        #Iterative Solution
        if not root:
            return []
        stack = [root]
        result = []

        while stack : 
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result 
        # t.c : O(n)
        # s.c : worst case scenario : O(n)
        # s.c : balanced :  O(logn)