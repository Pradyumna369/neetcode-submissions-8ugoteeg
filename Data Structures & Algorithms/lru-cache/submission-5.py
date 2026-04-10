class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.first = ListNode(-1, -1)
        self.last = ListNode(-1, -1)
        self.first.next = self.last
        self.last.prev = self.first

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.update(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
            self.update(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.first.next
            self.first.next = lru.next
            lru.next.prev = self.first
            del self.cache[lru.key]
    
    def update(self, node: ListNode) -> None:
        if node.next == self.last and node.prev:    # already most recent
            return
        if node.prev:
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev
        self.last.prev.next = node
        node.prev = self.last.prev
        self.last.prev = node
        node.next = self.last
        
        
