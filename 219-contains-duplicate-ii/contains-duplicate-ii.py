class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)) :
                if (nums[i]==nums[j] and abs(i-j)<=k):
                    return True
        return False

        #time limit exceeded
        '''
        # Hashmap DS
        seen ={}
        for i,num in enumerate(nums):
            if num in seen :
                if i-seen[num]<=k :
                    return True
            seen[num]=i
        return False