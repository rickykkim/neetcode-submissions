class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def add(self, node) -> None:
        curr = self.head.next
        node.prev = self.head
        node.next = curr
        curr.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # key already present, replace
        # key not present, check capacity and remove
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            curr = self.tail.prev
            self.remove(curr)
            del self.cache[curr.key]
        
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node

