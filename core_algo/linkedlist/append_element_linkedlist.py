class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

# recursive


def append(node: ListNode, target: int) -> ListNode:
    # Write your code here.
    if not node:
        return ListNode(target)

    node.next = append(node.next, target)

    return node

# iterative


def append2(node: ListNode, target: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = node
    p = dummy

    while p.next:
        p = p.next

    p.next = ListNode(target)

    return dummy.next


# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
LL2 = ListNode(1, ListNode(4, ListNode(5)))
print(arrayify(append(None, 1)))  # [1]
print(arrayify(append(LL1, 7)))  # [1, 4, 5, 7]
print(arrayify(append(ListNode(), 7)))  # [0, 7]
print(arrayify(append2(None, 1)))  # [1]
print(arrayify(append2(LL2, 7)))  # [1, 4, 5, 7]
print(arrayify(append2(ListNode(), 7)))  # [0, 7]
