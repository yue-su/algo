class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def arrayify(head) -> [int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def flip(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    second = head.next
    third = head.next.next

    second.next = head
    head.next = flip(third)

    return second



LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10, ListNode(11)))))))
print(arrayify(flip(None))) # [1]
print(arrayify(flip(ListNode(1)))) # [1]
print(arrayify(flip(ListNode(1, ListNode(2))))) # [2, 1]
print(arrayify(flip(LL1))) # [10, 7, 3, 5, 1, 13]
print(flip(None)) # None