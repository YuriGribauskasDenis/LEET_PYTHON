# 2.AddTwoNumbers.py
from leetcodelib import ListNode


def addTwoNumbers(l1, l2):
    some_node = ListNode()
    cur = some_node
    
    over = 0
    while l1 or l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        v = v1 + v2 + over
        over = v // 10
        v = v % 10
        cur.next = ListNode(v)
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        cur = cur.next
        
    if over:
        cur.next = ListNode(over)
        
    return some_node.next


print(addTwoNumbers(ListNode.lst2linklst([2,4,3]), ListNode.lst2linklst([5,6,4]))) # [7,0,8]
print(addTwoNumbers(ListNode.lst2linklst([0]), ListNode.lst2linklst([0]))) # [0]
print(addTwoNumbers(ListNode.lst2linklst([9,9,9,9,9,9,9]), ListNode.lst2linklst([9,9,9,9]))) # [8,9,9,9,0,0,0,1]