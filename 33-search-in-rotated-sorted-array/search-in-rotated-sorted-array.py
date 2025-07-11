class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums : 
            return nums.index(target)
        else :
            return -1

#Time Complexity : O(n)
# Space Complexity : O(1)