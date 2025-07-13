# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointer approach 
        """
        slow=head
        fast=head
        while fast and fast.next: # this while ensures that we dont assign fast to null:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True 
        return False """
        # approach with set 
        seen=set()
        while head:
            if head in seen:
                return True 
            seen.add(head)
            head=head.next
        return False
        
        