class ListNode:
    def __init__(self, key: None, value: None):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:
    '''
    cache = {
        1: 20,
        2: 20,
        3: 25
        }
        2 -> 3 -> 1
    '''

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
            node = self.cache[key]
        else:
            node = ListNode(key, value)
            self.cache[key] = node
        self.update(node)
        if len(self.cache) > self.capacity:
            lru = self.first.next
            del self.cache[lru.key]
            self.first.next = lru.next
            lru.next.prev = self.first
            
    def update(self, node: ListNode):
        if node.prev is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.last.prev.next = node
        node.prev = self.last.prev
        node.next = self.last
        self.last.prev = node




