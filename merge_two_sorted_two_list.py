from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return f"[{self.val}, {self.next}]"

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next
    
    if list1:
        current.next = list1
    
    if list2:
        current.next = list2

    return head.next

lst1 = [1, 2, 3, 4]
lst2 = [1, 4, 5, 6]

l1 = ListNode(lst1[0])
current = l1
for val in lst1[1:]: 
    current.next = ListNode(val)
    current = current.next

l2 = ListNode(lst2[0])
current = l2
for val in lst2[1:]: 
    current.next = ListNode(val)
    current = current.next

ret = mergeTwoLists(l1, l2)
print(ret)