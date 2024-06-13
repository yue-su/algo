class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# recursive


def sum_ll(node: ListNode) -> int:
    # Write your code here.
    if not node:
        return 0

    return node.value + sum_ll(node.next)


def sum_ll2(node: ListNode) -> int:
    res = 0
    while node:
        res += node.value
        node = node.next
    return res


# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum_ll(None))  # 0
print(sum_ll(LL1))  # 10
print(sum_ll(ListNode(1)))  # 1
print(sum_ll2(None))  # 0
print(sum_ll2(LL1))  # 10
print(sum_ll2(ListNode(1)))  # 1
