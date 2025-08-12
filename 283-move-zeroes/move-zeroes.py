class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0

        #Move all the non-zero elements to the end 
        for i in range (len(nums)):
            if nums[i]!=0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        
        #fill remaining position with zeros
        for i in range(lastNonZeroFoundAt,len(nums)):
            nums[i]=0