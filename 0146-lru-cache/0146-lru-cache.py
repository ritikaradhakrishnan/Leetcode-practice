#Key value but the value points to the node, easier to manage
#LRU, MRU nodes which have left, right pointers on each ends to the nodes (Doubly LL)
#Node is going to have key value + prev and next pointers

#we need remove and insert helper functions to keep track to Most recent and least

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        previousnode, nextnode = node.prev, node.next
        previousnode.next = nextnode
        nextnode.prev = previousnode

    def insert(self, node):
        previousmode, nextnode = self.right.prev, self.right
        previousmode.next = node
        nextnode.prev = node
        node.next, node.prev = nextnode, previousmode

        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
            #self[key] points to the node itself thats why we need val
        return -1

        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)