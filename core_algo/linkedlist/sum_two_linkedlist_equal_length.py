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


def sum_two_ll(head1: ListNode, head2: ListNode) -> ListNode:
    # Write your code here.
    if not head1 or not head2:
        return None
    
    head1.value += head2.value

    head1.next = sum_two_ll(head1.next, head2.next)

    return head1


# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(-1, ListNode(3, ListNode(-10)))
print(arrayify(sum_two_ll(LL1, LL2)))  # [0, 6, -5]
print(arrayify(sum_two_ll(ListNode(0), ListNode(0))))  # [0]
print(sum_two_ll(None, None))  # None
