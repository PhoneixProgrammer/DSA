class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1

        curr = ans = 0

        for num in nums :
            curr = curr + num
            ans = ans + counts[curr-k]
            counts[curr] += 1
        return ans
