class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# iterative
def count(node: ListNode) -> int:
    # Write your code here.
    p = node
    res = 0
    while p:
        res += 1
        p = p.next
    return res

# recursive
def count_recursive(node: ListNode) -> int:
    if not node:
        return 0

    return 1 + count_recursive(node.next)


# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None))  # 0
print(count(LL1))  # 3
print(count(ListNode()))  # 1
print(count_recursive(None))  # 0
print(count_recursive(LL1))  # 3
print(count_recursive(ListNode()))  # 1
