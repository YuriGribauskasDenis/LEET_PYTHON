# 61.RotateList.py
from leetcodelib import ListNode

def rotateRight(head, k):
    if not head:
        return head
    # get length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    k = k % length
    if k == 0:
        return head
    # rotate
    curr = head
    for _ in range(length - k - 1):
        curr = curr.next
    newHead = curr.next
    curr.next = None
    tail.next = head
    return newHead


print(rotateRight(ListNode.lst2linklst([1,2,3,4,5]), 2)) # [4,5,1,2,3]
print(rotateRight(ListNode.lst2linklst([0,1,2]), 4)) # [2,0,1]