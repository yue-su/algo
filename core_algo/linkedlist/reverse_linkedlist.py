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


def reverse(head: ListNode) -> ListNode:
    # Write your code here.
    if not head or not head.next:
        return head

    last = reverse(head.next)
    head.next.next = head
    head.next = None

    return last


def reverse2(head):
    if not head or not head.next:
        return head

    pre = None
    cur = head

    while cur:
        (cur.next,cur,pre)=(pre,cur.next,cur)

    return pre


# Test Cases
LL1 = ListNode(13, ListNode(1, ListNode(
    5, ListNode(3, ListNode(7, ListNode(10))))))
print(arrayify(reverse2(ListNode(1))))  # [1]
print(arrayify(reverse2(ListNode(1, ListNode(2)))))  # [2, 1]
print(arrayify(reverse2(LL1)))  # [10, 7, 3, 5, 1, 13]
print(reverse2(None))  # None
