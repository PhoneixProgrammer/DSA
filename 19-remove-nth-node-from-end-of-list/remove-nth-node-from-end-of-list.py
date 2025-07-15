# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = slow = dummy

        #Move fast pointer n+1 steps ahead
        for _ in range(n+1):
            fast = fast.next

        #Move fast to the end, slow will reach node before the target
        while fast :
            fast = fast.next
            slow = slow.next

        #remove the nth node from end 
        slow.next = slow.next.next

        return dummy.next

        #time complexity : O(N)
        #space complexity : O(1)
