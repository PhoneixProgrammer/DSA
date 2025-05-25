class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+1): # [1,8]
            if i in nums:
                nums.remove(i)
            else :
                nums.add(i)
        return list(nums)