class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums=[]
        seen=set()

        for num in nums :
            if num not in seen:
                seen.add(num)
                unique_nums.append(num)
        unique_nums = sorted(unique_nums, reverse=True)
        if len(unique_nums)>2:
            return unique_nums[2]
        else:
            return max(unique_nums)