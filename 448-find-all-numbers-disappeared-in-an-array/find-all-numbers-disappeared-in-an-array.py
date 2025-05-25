class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark numbers as seen by negating the value at the corresponding index
        for num in nums:
            index = abs(num) - 1  # Convert value to index (1-based to 0-based)
            if nums[index] > 0:
                nums[index] = -nums[index]  # Mark as seen (by making it negative)
        #print(nums)

        # Step 2: Collect indices where values are still positive
        # These indices + 1 are the numbers that were missing
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
        '''
        n=len(nums)
        nums=set(nums)
        for i in range(1,n+1): # [1,8]
            if i in nums:
                nums.remove(i)
            else :
                nums.add(i)
        return list(nums)
        #t.c and s.c : O(n)
        '''

        