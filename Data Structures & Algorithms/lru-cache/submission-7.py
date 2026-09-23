class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next= self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    
    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        # node already present -> update
        # node not present -> 1) < capacity and 2) == capacity
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            node = self.tail.prev
            self.remove(node)
            del self.cache[node.key]
        
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
