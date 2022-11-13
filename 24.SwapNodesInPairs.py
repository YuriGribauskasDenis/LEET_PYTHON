# 24.SwapNodesInPairs.py
from leetcodelib import ListNode

def swapPairs(head):
    dummy = ListNode(-69, head)
    prev = dummy
    curr = head
    while curr and curr.next:
        nextPair = curr.next.next
        second = curr.next
        #========================
        second.next = curr
        curr.next = nextPair
        prev.next = second
        #========================
        prev = curr
        curr = nextPair
    return dummy.next


print(swapPairs(ListNode.lst2linklst([1,2,3,4]))) # [2,1,4,3]
print(swapPairs(ListNode.lst2linklst([1,2,3,4,5]))) # [2,1,4,3,5]
print(swapPairs(ListNode.lst2linklst([]))) # []
print(swapPairs(ListNode.lst2linklst([1]))) # [1]