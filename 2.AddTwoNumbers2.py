# 2.AddTwoNumbers.py
from leetcodelib import ListNode


def addTwoNumbers(l1, l2):
    dummy = ListNode(-69)
    tail = dummy
    
    one = 0
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        v = v1 + v2 + one
        one = v // 10
        v = v % 10
        tail.next = ListNode(v)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        tail = tail.next
    
    if one:
        tail.next = ListNode(one)
    
    return dummy.next


print(addTwoNumbers(ListNode.lst2linklst([2,4,3]), ListNode.lst2linklst([5,6,4]))) # [7,0,8]
print(addTwoNumbers(ListNode.lst2linklst([0]), ListNode.lst2linklst([0]))) # [0]
print(addTwoNumbers(ListNode.lst2linklst([9,9,9,9,9,9,9]), ListNode.lst2linklst([9,9,9,9]))) # [8,9,9,9,0,0,0,1]