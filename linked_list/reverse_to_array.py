class Node:
    def __init__(self, value, next=None):
       self.val = value
       self.next = next

def createArrayInReverse(node: Node) -> list[int]:
    res = []

    def helper(node):
        if node is None:
            return
        
        helper(node.next)
        res.append(node.val)

    helper(node)

    return res



# 1 -> 3 -> 5 -> 2
head = Node(1, Node(3, Node(5, Node(2))))
print(createArrayInReverse(head) == [2, 5, 3, 1])

# 4 -> 9 -> 14
head = Node(4, Node(9, Node(14)))
print(createArrayInReverse(head) == [14, 9, 4])

# 5 -> 10 -> 15 -> 20
head = Node(5, Node(10, Node(15, Node(20))))
print(createArrayInReverse(head) == [20, 15, 10, 5])

# 5
head = Node(5)
print(createArrayInReverse(head) == [5])

# 5 -> 10
head = Node(5, Node(10))
print(createArrayInReverse(head) == [10, 5])

# 5 -> 5 -> 10 -> 10
head = Node(5, Node(5, Node(10, Node(10))))
print(createArrayInReverse(head) == [10, 10, 5, 5])

# 5 -> 5 -> 5
head = Node(5, Node(5, Node(5)))
print(createArrayInReverse(head) == [5, 5, 5])

# 0
head = Node(0)
print(createArrayInReverse(head) == [0])

# None
head = None
print(createArrayInReverse(head) == [])