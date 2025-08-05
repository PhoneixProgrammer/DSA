class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Data structure  --> Hashmap 

        seen = {}

        for i, num in enumerate(nums):
            if num  in seen and abs(i-seen[num])<=k :
                return True
            seen[num] = i
        return False