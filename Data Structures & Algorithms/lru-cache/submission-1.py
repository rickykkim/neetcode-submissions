class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.recent = deque()
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.recent.remove(key)
            self.recent.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.recent.remove(key)
            self.recent.append(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                del_key = self.recent.popleft()
                del self.cache[del_key]
            self.recent.append(key)
            self.cache[key] = value
