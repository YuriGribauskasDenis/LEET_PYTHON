
# 25.ReverseNodesInk-Group.py
from leetcodelib import ListNode

def reverseKGroup(head, k):
    dummy = ListNode(-69, head)
    groupPrev = dummy
    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next
    
        prev = kth.next
        curr = groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    
    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


print(reverseKGroup(ListNode.lst2linklst([1,2,3,4,5]), 2)) # [2,1,4,3,5]
print(reverseKGroup(ListNode.lst2linklst([1,2,3,4,5]), 3)) # [3,2,1,4,5]