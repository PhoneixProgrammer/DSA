# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        #recursive solution
        if root is None :
            return None
        
        #swap the left and right children
        root.left, root.right = root.right, root.left 

        #recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        '''
        #Iterative Approach
        if root is None:
            return None

        queue = deque([root])

        while queue:
            current = queue.popleft()

            #swap the left and right children
            current.left, current.right = current.right, current.left 

            #add children to the queue if they exist
            if current.left :
                queue.append(current.left)
            if current.right :
                queue.append(current.right)
        return root

        #time complexity :O(n)
        #space complexity :O(n)
