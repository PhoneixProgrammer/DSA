class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        res=set()
        for item in nums1:
            if item in nums2:
                res.add(item)
        return list(res)
        '''
#time complexity : O(n*m) which is not a optimal solution

        return list(set(nums1) & set(nums2))
        #Optimal Solution
        