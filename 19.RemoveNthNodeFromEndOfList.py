# 19.RemoveNthNodeFromEndOfList.py
from leetcodelib import ListNode

def removeNthFromEnd(head, n):
    dummy = ListNode(-69, head)
    left = dummy
    right = head
    for _ in range(n):
        right = right.next
    # while n > 0 and right:
    #     right = right.next
    #     n -= 1
    while right:
        right = right.next
        left = left.next
    left.next = left.next.next
    return dummy.next


print(removeNthFromEnd(ListNode.lst2linklst([1,2,3,4,5]), 2)) # [1,2,3,5]
print(removeNthFromEnd(ListNode.lst2linklst([1]), 1)) # []
print(removeNthFromEnd(ListNode.lst2linklst([1,2]), 1)) # [1]