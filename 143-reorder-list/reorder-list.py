# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next :
            return 

        #Step 1:  Find the middle element of the list
        slow, fast = head, head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        #Step 2: reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None #Break the list into 2 halves
        while curr :
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        #Step3: Merge the 2halves alternatively 
        first,second = head, prev
        while second : 
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next =  tmp1
            first,second = tmp1,tmp2