# 23.MergeKSortedLists.py
from leetcodelib import ListNode

# exlpicit list to linked list conversion
# and vice versa
def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            li1 = ListNode.lst2linklst(l1)
            li2 = ListNode.lst2linklst(l2)
            ml = mergeLists(li1, li2)
            ml = lnklst2lst(ml)
            mergedLists.append(ml)
        lists = mergedLists
    return lists[0]

def lnklst2lst(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def mergeLists(lst1, lst2):
    dummy = ListNode(-69)
    tail = dummy
    while lst1 and lst2:
        if lst1.val < lst2.val:
            tail.next = lst1
            lst1 = lst1.next
        else:
            tail.next = lst2
            lst2 = lst2.next
        tail = tail.next
    if lst1:
        tail.next = lst1
    if lst2:
        tail.next = lst2
    return dummy.next


a1 = [[1,4,5],[1,3,4],[2,6]]
# al1 = [ListNode.lst2linklst(a) for a in a1]
print(mergeKLists(a1)) # [1,1,2,3,4,4,5,6]

a1 = []
# al1 = [ListNode.lst2linklst(a) for a in a1]
print(mergeKLists(a1)) # []

a1 = [[]]
# al1 = [ListNode.lst2linklst(a) for a in a1]
print(mergeKLists(a1)) # []