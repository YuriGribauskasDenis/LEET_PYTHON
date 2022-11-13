# 83.RemoveDuplicatesFromSortedList.py
from leetcodelib import ListNode

def deleteDuplicates(head):
    curr = head
    while curr:
        while curr.next and curr.val == curr.next.val:
            curr.next = curr.next.next
        curr = curr.next
    return head


print(deleteDuplicates(ListNode.lst2linklst([1,1,2]))) # [1,2]
print(deleteDuplicates(ListNode.lst2linklst([1,1,2,3,3]))) # [1,2,3]
print(deleteDuplicates(ListNode.lst2linklst([1,1,1,3,3]))) # [1,3]
print(deleteDuplicates(ListNode.lst2linklst([]))) # []