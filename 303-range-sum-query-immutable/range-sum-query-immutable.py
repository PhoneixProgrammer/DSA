class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum=[0]
        for num in nums : 
            self.prefixSum.append(self.prefixSum[-1]+num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1]-self.prefixSum[left]
#Initialization: O(n) time and O(n) space
#Each sumRange query: O(1) time and O(1) extra space

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)