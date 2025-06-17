class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:

        good_num = []
        n = len(nums)

        for i in range(n):
            left_exists = (i - k) >= 0
            right_exists = (i + k) < n

            if left_exists and right_exists:
                if nums[i] > nums[i - k] and nums[i] > nums[i + k]:
                    good_num.append(nums[i])
            elif left_exists:
                if nums[i] > nums[i - k]:
                    good_num.append(nums[i])
            elif right_exists:
                if nums[i] > nums[i + k]:
                    good_num.append(nums[i])
            else:
                # Neither index exists → nums[i] is good
                good_num.append(nums[i])
        
        res=0
        for i in range(len(good_num)):
            res = res + good_num[i]
        return res

        # time complexity :O(n)
        # space complexity : O(n)