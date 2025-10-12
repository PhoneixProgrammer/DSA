class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1

        #Step 1 : Find the pivot 
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1] :
                pivot = i
                break
        
        if pivot == -1 :
            #Array is in descending order, reverse it
            nums.reverse()
            return

        #step 2 : Find the smallest number bigger than pivot to swap
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot] :
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        #Step 3: Reverse the part after pivot
        left, right  = pivot + 1, n-1
        while left < right :
            nums[left], nums[right] = nums[right],nums[left]
            left += 1
            right -= 1