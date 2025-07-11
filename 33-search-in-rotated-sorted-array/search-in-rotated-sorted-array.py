class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #O(logn) solution
        if not nums :
            return -1

        left, right =  0, len(nums)-1

        #Find pivot (smallest element index)
        while left < right :
            mid = (left+right)//2 
            if nums[mid] > nums[right]:
                left = mid + 1
            else :
                right = mid
        pivot = left

        #Decide which half to binary search
        left, right = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else : 
            right = pivot -1 

        #standard binary search 
        while left <= right :
            mid =(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target :
                left = mid +1
            else:
                right = mid-1
        return -1