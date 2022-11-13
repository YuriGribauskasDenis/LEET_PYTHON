# 86.PartitionList.py
from leetcodelib import ListNode

def partition(head, x):
    left = ListNode(-69)
    right = ListNode(-69)
    ltail = left
    rtail = right
    while head:
        if head.val < x:
            ltail.next = head
            ltail = ltail.next
        else:
            rtail.next = head
            rtail = rtail.next
        head = head.next
    ltail.next = right.next
    rtail.next = None
    return left.next


print(partition(ListNode.lst2linklst([1,4,3,2,5,2]), 3)) # [1,2,2,4,3,5]
print(partition(ListNode.lst2linklst([2,1]), 2)) # [1,2]