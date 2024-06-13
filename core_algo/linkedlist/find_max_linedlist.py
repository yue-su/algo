class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def find_max(node: ListNode) -> int:
    # Write your code here.
    if not node:
        return 0

    max_next = find_max(node.next)
    return max(max_next, node.value)


def find_max2(node):
    max_val = 0
    while node:
        max_val = max(max_val, node.value)
        node = node.next
    return max_val


# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(find_max(LL1))  # 5
print(find_max(LL2))  # 7
print(find_max(LL3))  # 0
print(find_max(ListNode(1)))  # 1
print(find_max2(LL1))  # 5
print(find_max2(LL2))  # 7
print(find_max2(LL3))  # 0
print(find_max2(ListNode(1)))  # 1
