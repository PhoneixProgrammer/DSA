from typing import List

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta=1):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def greater_than(self, i):
        return self.query(self.n) - self.query(i)


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums

        # Coordinate compression
        sorted_unique = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}

        ft1 = FenwickTree(len(sorted_unique))
        ft2 = FenwickTree(len(sorted_unique))

        first = [nums[0]]
        second = [nums[1]]

        ft1.update(rank[nums[0]])
        ft2.update(rank[nums[1]])

        for i in range(2, len(nums)):
            r = rank[nums[i]]

            g1 = ft1.greater_than(r)
            g2 = ft2.greater_than(r)

            if g1 > g2:
                first.append(nums[i])
                ft1.update(r)
            elif g2 > g1:
                second.append(nums[i])
                ft2.update(r)
            else:
                if len(first) <= len(second):
                    first.append(nums[i])
                    ft1.update(r)
                else:
                    second.append(nums[i])
                    ft2.update(r)

        return first + second
