class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

#postorder traversal
def kth_from_last(head: ListNode, k: int) -> int:

    if not head:
        return None
    # Write your code here.

    def helper(head):
        if not head:
            return 0, -1

        index, value = helper(head.next)
        index += 1
        if index == k:
            return index, head.value

        return index, value

    _, value = helper(head)

    return value

# don't try to do fancy one loop


def kth_from_last2(head, k):
    if not head:
        return None

    fast = slow = head

    for _ in range(k):
        if not fast:
            return -1
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.value


# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(
    5, ListNode(3, ListNode(7, ListNode(10))))))
print(kth_from_last(LL1, 1))  # 10
print(kth_from_last(LL1, 3))  # 3
print(kth_from_last(LL1, 6))  # 13
print(kth_from_last(LL1, 7))  # -1
print(kth_from_last(None, 7))  # None
