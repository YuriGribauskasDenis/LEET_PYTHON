# 86.PartitionList.py
from leetcodelib import ListNode

def partition(head, x):
    left = ListNode(-69)
    dummy = left
    right = ListNode(-69)
    tmp = right
    curr = head
    while curr:
        if curr.val < x:
            left.next = ListNode(curr.val)
            left = left.next
        else:
            right.next = ListNode(curr.val)
            right = right.next
        curr = curr.next
    left.next = tmp.next
    return dummy.next


print(partition(ListNode.lst2linklst([1,4,3,2,5,2]), 3)) # [1,2,2,4,3,5]
print(partition(ListNode.lst2linklst([2,1]), 2)) # [1,2]