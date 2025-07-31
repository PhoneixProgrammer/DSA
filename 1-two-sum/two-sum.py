class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic_map = {}

        for i, num in enumerate(nums):
            complement = target-num
            if complement in dic_map :
                return [dic_map[complement],i]
            dic_map[num] = i

        '''Time Complexity :
        1. i traverse the nums ,each digit is visited so if there are n didgits it will take O(n) time
        2. each lookup and insertion in dictionary is O(1) time
        
        so total average :  O(n)
        '''

        '''Space Complexity :
        in worst case, you may store all n elements in dictionary so O(n)
        '''