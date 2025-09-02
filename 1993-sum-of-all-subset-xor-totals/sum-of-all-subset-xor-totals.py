class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if  not nums :
             return 0 

        or_val = 0 
        for x in nums :
            or_val |= x
        return or_val * (1 << (len(nums)-1))