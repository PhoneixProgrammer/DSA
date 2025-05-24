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
        for i,num in enumerate(nums): # this takes O(n) time
            if num in seen : # O(1) because hashmap
                if i-seen[num]<=k : #O(1)
                    return True
            seen[num]=i #O(1)
            ##print(seen)
        return False
        # Time complexity : O(n)
        #Space Complexity : O(n)
        # because in worst case scenario if all the elements in the nums is distinct then it stores each element in the seen which is a dict
        # so it stores each value with its index , if you have 1 billion elements in the array , its stores 1 billion value to its index value