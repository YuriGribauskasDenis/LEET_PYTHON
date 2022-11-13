# 92.ReverseLinkedListII.py
from leetcodelib import ListNode

def reverseBetween(head, left, right):
    # T O(n)
    # M O(1)
    dummy = ListNode(-69, head)
    # find
    leftprev = dummy
    curr = dummy.next
    for _ in range(left - 1):
        leftprev = curr
        curr = curr.next
    #reverse
    prev = None
    for _ in range(right - left + 1):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    # connect
    leftprev.next.next = curr
    leftprev.next = prev
    return dummy.next


print(reverseBetween(ListNode.lst2linklst([1,2,3,4,5]), 2, 4)) # [1,4,3,2,5]
print(reverseBetween(ListNode.lst2linklst([5]), 1, 1)) # [5]