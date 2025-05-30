class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # End of current range
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        # Handle the last range after the loop
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result

        #Time Complexity: O(n)
        #-->You go through the list once.
        #-->Each element is visited exactly once.
        #-->No nested loops or repeated work.

        #Space Complexity: O(1) 