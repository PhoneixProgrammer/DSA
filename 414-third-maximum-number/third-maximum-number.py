class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums=[]
        seen=set()

        for num in nums :#O(n)  time
            if num not in seen:
                seen.add(num)
                unique_nums.append(num)
        unique_nums = sorted(unique_nums, reverse=True) #O(nlogn)
        if len(unique_nums)>2: #O(1)
            return unique_nums[2]
        else:
            return max(unique_nums)

        #t.c : O(nlogn)