class MedianFinder:

    def __init__(self):
        #Initilize an empty list to store numbers
        self.data = []

    def addNum(self, num: int) -> None:
        #Add the number to the list
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        return statistics.median(self.data)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()