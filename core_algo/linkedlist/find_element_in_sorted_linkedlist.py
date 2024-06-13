class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def search(head: ListNode, target: int) -> bool:
    # Write your code here.
    if not head:
        return False

    if head.value > target:
        return False

    return head.value == target or search(head.next, target)


def search2(head, target):
    if not head:
        return False
    while head:
        if head.value > target:
            return False
        if head.value == target:
            return True
        head = head.next

    #edge case, when search reach the end and not found
    return False


# Test Cases
LL1 = ListNode(1, ListNode(2, ListNode(
    3, ListNode(5, ListNode(6, ListNode(7, ListNode(10)))))))
print(search2(None, 1))  # False
print(search2(LL1, 2))  # True
print(search2(LL1, 4))  # False
print(search2(LL1, -1))  # False
print(search2(LL1, 10))  # True
print(search2(LL1, 11))  # False
