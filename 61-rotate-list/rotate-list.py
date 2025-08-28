# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge cases : empty list, single node or no rotation
        if not head or not head.next or k == 0:
            return head

        # --------------------------------
        # Step 1: Find the length and tail
        # -------------------------------
        length = 1
        tail = head
        while tail.next :
            tail = tail.next 
            length+=1

        # ---------------------------------
        # Step 2: Make it circular
        # ---------------------------------
        tail.next = head #connect last node to the head

        #-----------------------------------
        # Step 3 : Find the new head position
        # -----------------------------------
        k = k % length # incase k > length
        steps_to_new_head = length - k #move this many steps from start

        # ----------------------------------
        # Step 4 : Walk to the new tail
        # ----------------------------------
        new_tail = head 
        for _ in range(steps_to_new_head - 1): #stop just before new head
            new_tail = new_tail.next

        # ---------------------------------
        # Step 5 : Break the circle 
        # ---------------------------------
        new_head = new_tail.next 
        new_tail.next = None

        return new_head

        #Time Complexity : O(n)
        #Space Complexity : O(1)