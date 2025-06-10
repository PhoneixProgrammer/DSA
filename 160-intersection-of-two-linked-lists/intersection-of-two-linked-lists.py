# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA, pB =  headA, headB

        #traverse until both pointers met or reach the end(None)
        while pA is not pB:
            # move to the next node or jump to other list's head if at the end
            if pA is not None :
                pA = pA.next
            else :
                pA = headB
            
            if pB is not None :
                pB = pB.next
            else :
                pB = headA
        return pA

