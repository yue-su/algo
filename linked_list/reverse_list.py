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

def reverse(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    new_head = reverse(head.next)
    #when head.next == 10, reverse(10) will return 10 to the reverse(9), so here the head is 9, which is the second last
    head.next.next = head
    head.next = None
    
    return new_head

LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(arrayify(reverse(ListNode(1)))) # [1]
print(arrayify(reverse(ListNode(1, ListNode(2))))) # [2, 1]
print(arrayify(reverse(LL1))) # [10, 7, 3, 5, 1, 13]
print(reverse(None)) # None