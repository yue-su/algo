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


def insert(head: ListNode, target: int) -> ListNode:
    # Write your code here.
    if not head:
        return ListNode(target)

    if target < head.value:
        new_head = ListNode(target)
        new_head.next = head
        return new_head

    head.next = insert(head.next, target)
    return head


def insert2(head, target):
    dummy = ListNode(-1)
    dummy.next = head
    p = dummy

    while p.next and target > p.next.value:
        p = p.next

    if p.next:
        temp = p.next
        p.next = ListNode(target)
        p.next.next = temp
    else:
        p.next = ListNode(target)    

    return dummy.next


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(4)))
LL2 = ListNode(-3, ListNode(-2, ListNode(-1)))
print(arrayify(insert2(LL1, 2)))  # [1, 2, 3, 4]
print(arrayify(insert2(LL2, -4)))  # [-4, -3, -2, -1]
print(arrayify(insert2(LL2, 0)))  # [-3, -2, -1, 0]
print(arrayify(insert2(None, 1)))  # [1]
