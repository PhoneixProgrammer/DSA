class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_map = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement in dict_map :
                return [dict_map[complement],i]
            dict_map[num] = i

        #Time Complexity and Space Complexity is O(n)