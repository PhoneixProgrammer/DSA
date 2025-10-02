class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for num in nums :
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

        # Complexities  :
        # 1. Heap push/pop = O(logk) each
        # 2. For n elemnst = O(nlogk)
        # 3. Space = O(k)