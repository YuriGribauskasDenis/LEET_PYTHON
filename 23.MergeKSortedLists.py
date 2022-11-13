# 23.MergeKSortedLists.py

# leetcode version where list to linked list
# and vice versa is done implicitly
def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeLists(l1, l2))
        lists = mergedLists
    return lists[0]

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