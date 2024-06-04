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
    
    pre_last = None
    last = head
    
    while last.next:
        pre_last = last
        last = last.next

    if pre_last is head:
        last.next = head
        head.next = None

    pre_last.next = head
    last.next = head.next
    head.next = None

    return last





LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(arrayify(flip(None))) # [1]
print(arrayify(flip(ListNode(1)))) # [1]
print(arrayify(flip(ListNode(1, ListNode(2))))) # [2, 1]
print(arrayify(flip(LL1))) # [10, 7, 3, 5, 1, 13]
print(flip(None)) # None