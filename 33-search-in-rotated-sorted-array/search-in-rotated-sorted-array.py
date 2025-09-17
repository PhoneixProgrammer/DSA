class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums :
            return -1

        left , right  = 0, len(nums)-1

        #step 1: finding the pivot point(smallest elemnt index)
        while left < right :
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else :
                right = mid 
        pivot = left

        #step 2: decide which half to do bianry search
        left, right = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot 
        else :
            right = pivot - 1

        #step 3 : standard bianry search 
        while left <=  right :
            mid = (left+right)//2
            if nums[mid] == target :
                return mid
            elif nums[mid] <  target :
                left = mid + 1
            else :
                right = mid-1
        return -1 


        #time complexity for pivort search is O(logn)
        # time complexity for binary search is O(logn)
        #Space Complexity : O(1)


