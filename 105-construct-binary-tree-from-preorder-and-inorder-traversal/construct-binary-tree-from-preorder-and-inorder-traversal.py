# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder : 
            return None

        #Build a hashmap to store value -- > index for quick lookup in inorder
        inorder_index_map = {val:idx for idx,val in enumerate(inorder)}

        #Pointer to the crrent root in preorder
        preorder_index = 0

        def helper(left,right):
            nonlocal preorder_index
            if left > right :
                return None

            #Get root value and create the node
            root_val = preorder[preorder_index]
            root =  TreeNode(root_val)

            #Increment preorder index
            preorder_index += 1

            #Build left and right subtreess
            root.left = helper(left,inorder_index_map[root_val] -1)
            root.right = helper(inorder_index_map[root_val] + 1, right)

            return root

        return helper(0,len(inorder)-1)