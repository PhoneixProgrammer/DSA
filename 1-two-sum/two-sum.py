class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Hash Map - O(1)
        dic={}
        for i in range(len(nums)):
            num=nums[i]
            complement=target-num
            if complement in dic:
                return [i,dic[complement]]
            dic[num]=i
            #hashmap :ds
        return [-1,1]