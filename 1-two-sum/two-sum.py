class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_map  = {}

        for i in range(len(nums)) :
            complement = target - nums[i] 
            if complement in dict_map :
                return [dict_map[complement],i]
            dict_map[nums[i]] = i
        