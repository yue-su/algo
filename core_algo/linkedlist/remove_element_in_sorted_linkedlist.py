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


def remove(head: ListNode, target: int) -> ListNode:
    # Write your code here.
    if not head:
        return head

    if target < head.value:
        return head

    if head.value == target:
        return head.next

    head.next = remove(head.next, target)

    return head


def remove2(head, target):
    if head.value == target:
        return head.next

    curr = head
    while curr.next and curr.next.value <= target:
        if curr.next.value == target:
            curr.next = curr.next.next
            return head
        curr = curr.next

    return head


# Test Cases
LL1 = ListNode(-1, ListNode(1, ListNode(3, ListNode(4))))
print(arrayify(remove2(LL1, 1)))  # [-1, 3, 4]
LL1 = remove2(LL1, -1)  # Notice we expect this one to return a new head!
print(arrayify(LL1))  # [3, 4]
print(arrayify(remove2(LL1, 4)))  # [3]
print(arrayify(remove2(LL1, 5)))  # [3]
print(arrayify(remove2(ListNode(1), 1)))  # []
