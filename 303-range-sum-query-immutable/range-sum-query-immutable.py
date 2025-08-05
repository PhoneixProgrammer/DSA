class NumArray:

    def __init__(self, nums: List[int]):
        self.arr :List[int] = nums

    def sumRange(self, left: int, right: int) -> int:
        result = sum(self.arr[left:right+1])
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)