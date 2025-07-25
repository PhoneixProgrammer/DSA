class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # only start counting if num is the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest

        #T.c : O(n)
        #S.c : O(n)
