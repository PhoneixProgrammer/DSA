class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dictionary = OrderedDict()
    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        self.dictionary.move_to_end(key)
        return self.dictionary[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary :
            self.dictionary.move_to_end(key)
        self.dictionary[key] = value
        if len(self.dictionary) > self.capacity :
            self.dictionary.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)