# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Brute force Approach 
        # Approach is each node in each of the linked list , i am adding to an array
        # i sort the array
        # that array i convert it to linked list of nodes 
        nodes = []
        head = point = ListNode(0)

        for l in lists:
            while l :
                nodes.append(l.val)
                l =l.next
        
        for x in sorted(nodes):
            point.next = ListNode(x)
            point =  point.next 
        
        return head.next

        #Time Complexity : O(NlogN)
        #Space Complexity :O(N) cost 