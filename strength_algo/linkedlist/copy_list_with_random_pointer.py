'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Construct a deep copy of the list with a random pointer. View prompt details.
https://leetcode.com/problems/copy-list-with-random-pointer/description/


▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
'''


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        if not head:
            return None

        p = head
        while p:
            nodes[p] = Node(p.val)
            p = p.next

        p = head
        while p:
            if p.next:
                nodes[p].next = nodes[p.next]
            if p.random:
                nodes[p].random = nodes[p.random]
            p = p.next

        return nodes[head]


# Test Cases
test.startProblem("Copy List with Random Pointer")
p4 = Node(4, None)
p3 = Node(3, p4)
p2 = Node(2, p3)
p1 = Node(1, p2)
p1.random = p4
p2.random = p1
p3.random = p1
p4.random = None
copied = copyRandomList(p1)
test.test(copied.value, 1, 1)
test.test(copied.random.value, 4, 2)
test.test(copied.next.value, 2, 3)
test.test(copied.next.random.value, 1, 4)
test.test(copied.next.next.value, 3, 5)
test.test(copied.next.next.random.value, 1, 6)
test.test(copied.next.next.next.value, 4, 7)
test.test(copied.next.next.next.random, None, 8)
test.endProblem()
