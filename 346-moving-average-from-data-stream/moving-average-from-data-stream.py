class MovingAverage:

    def __init__(self, size: int):
        self.windowSize =  size
        self.arr = []

    def next(self, val: int) -> float:
        arr = self.arr
        windowSize = self.windowSize
        arr.append(val)
        
        return sum(arr[-windowSize:])/min(len(arr),windowSize)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)