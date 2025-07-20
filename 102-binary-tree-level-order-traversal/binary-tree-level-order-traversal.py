# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : 
            return []

        result =[] #final answer : list of lists
        queue = deque([root]) # initialize queu with root node for BFS

        while queue :
            level_size = len(queue) # Number of nodes at the current level
            level_nodes = [] #list to hold current level's node values

            for _ in range(level_size):
                node =  queue.popleft() #pop from the front of the queue
                level_nodes.append(node.val)

                #enqueue left and right children (next level)
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)

            result.append(level_nodes) #append this level results 
        return result

        #Time Complexity : O(n)
        #Space Complexity : O(n) (in worst case each node is stored level by level)
