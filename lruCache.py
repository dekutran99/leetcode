class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.usage = []

    def get(self, key: int) -> int:
        value = -1
        
        if key in self.data:
            value = self.data[key]
            self.usage.remove(key)
            self.usage.insert(0, key)
        
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            self.usage.remove(key)
            self.usage.insert(0, key)
        else:
            if len(self.data) == self.capacity:
                lruKey = self.usage.pop()
                self.data.pop(lruKey)
            self.data[key] = value
            self.usage.insert(0, key)

'''
This is assuming that we are NOT using ordered set/dictionary, which is built into Python.
If we use ordered set/dictionary, we can truly achieve O(1) time complexity for get() and put().
'''