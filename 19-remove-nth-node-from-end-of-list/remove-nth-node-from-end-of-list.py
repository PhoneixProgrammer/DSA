# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #edge cases like when you want to delete first node in the linkedlist
        # 
        dummy = ListNode(0, head)
        fast = slow = dummy

        #move fast n+1 steps ahead
        for _ in range(n+1):
            fast = fast.next 

        # move both pointers until fast reaches the end 
        while fast :
            fast = fast.next
            slow = slow.next
        
        # 1 ->  2 - > 3-   >4 -  >5 -->None
        #             slow             fast
        
        #delete the node
        slow.next= slow.next.next

        return dummy.next

        # t.c : O(n)
        #s.c : O(1)

