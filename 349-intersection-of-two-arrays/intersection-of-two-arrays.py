class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set()
        for item in nums1:
            if item in nums2:
                res.add(item)
        return list(res)
