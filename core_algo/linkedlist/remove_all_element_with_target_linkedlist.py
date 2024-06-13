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


def remove(node: ListNode, target: int) -> ListNode:
    if not node:
        return None

    if node.value == target:
        return remove(node.next, target)

    node.next = remove(node.next, target)

    return node


def remove3(node, target):
    dummy = ListNode(-1)
    dummy.next = node
    p = dummy

    while p and p.next:
        if p.next.value == target:
            p.next = p.next.next
        else:
            p = p.next

    return dummy.next

# postorder traversal
def remove2(node, target):
    if not node:
        return None
    
    #node is the last node
    node.next = remove2(node.next, target)
    if node.value == target:
        return node.next
    
    return node


# Test Cases
LL1 = ListNode(4, ListNode(2, ListNode(
    1, ListNode(1, ListNode(3, ListNode(2, ListNode(2)))))))
LL2 = remove2(None, 1)
print(arrayify(LL2))  # []
LL1 = remove2(LL1, 1)
print(arrayify(LL1))  # [4, 2, 3, 2, 2]
LL1 = remove2(LL1, 2)
print(arrayify(LL1))  # [4, 3]
remove2(LL1, 3)
print(arrayify(LL1))  # [4]
LL1 = remove2(LL1, 4)
print(arrayify(LL1))  # []
