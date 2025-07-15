# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0  # Unique index to break ties

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next    

        # time complexity is O(Nlogk)
        # space complexity is O(k)