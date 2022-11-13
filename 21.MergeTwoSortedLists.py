# 21.MergeTwoSortedLists.py
from leetcodelib import ListNode

def mergeTwoLists(list1, list2):
    dummy = ListNode(-69)
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return dummy.next


print(mergeTwoLists(ListNode.lst2linklst([1,2,4]), ListNode.lst2linklst([1,3,4]))) # [1,1,2,3,4,4]
print(mergeTwoLists(ListNode.lst2linklst([]), ListNode.lst2linklst([]))) # []
print(mergeTwoLists(ListNode.lst2linklst([]), ListNode.lst2linklst([0]))) # [0]