# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        if not nums:
            return None

        mid = len(nums)//2
        root = TreeNode(nums[mid])

        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])

        return root

        '''

        # Solution 1:  recursive divide and conquer using slicing 
        # time complexity :  O(n)
        # Space complexity : O(nlogn) becacuase of the slicing
        # it creates new array at each step which add this memory 
        # overhead

        def helper(left:int, right:int)->Optional[TreeNode]:
            if left > right :
                return None
            
            mid= (left+right)//2
            root=TreeNode(nums[mid])
            root.left= helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root

        return helper(0,len(nums)-1)

        #Opitimal solution for saving space 
        #Time Complexity  =O(n)
        #Space Complexity = O(logn) 
