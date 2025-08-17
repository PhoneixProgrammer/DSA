class RandomizedSet:

    def __init__(self):
        self.arr =[]
        self.set= set()
    def insert(self, val: int) -> bool:
        if val not in self.set : #check in O(1)
            self.arr.append(val)
            self.set.add(val)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        if val in self.set:
            self.arr.remove(val)
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()