# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# ✏️ Description
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
# Q. Design a data structure that follows the constraints of a Least Recently Used(LRU) cache.

# Implement the LRUCache class .

# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Examples:
# See test cases.
# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# 🟦 Python
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

'''
take aways:
1. using two dummy node to handle edge cases
2. a Node can hold move than one value
3. Move a node to the head could be considered two steps: a) remove the node 2) add to the head
4. handle next and prev in pairs
'''


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        else:
            return None

    def put(self, key: int, val: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, val)
        # when reach to capacity
        if len(self.cache) == self.capacity:
            self._evict()
        self.cache[key] = node
        self._add_to_head(node)

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        # MISTAKE needed to handle the prev for the old head!!
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None

    def _evict(self):
        self.cache.pop(self.tail.prev.key)
        self._remove(self.tail.prev)

    def print_ll(self):
        ll = []
        p = self.head
        while p:
            ll.append(p.value)
            p = p.next
        print(ll)


# Test Cases
cache = LRUCache(3)
print(cache.get(0))  # None
cache.put(1, 10)
# cache.print_cache()
cache.put(2, 20)
cache.put(3, 30)
print(cache.get(1))  # 10
print(cache.get(2))  # 20
cache.put(key=4, val=40)

print(cache.get(3))  # None because purged when 4 was put in.
cache.print_ll()
cache.put(key=5, val=50)
print(cache.get(1))
