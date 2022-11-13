# linkedlistlib.py
from __future__ import annotations
from typing import List

class ListNode:
    """
    A class used to build a Linked List
    The class is a List Node representation

    ...

    Attributes
    ----------
    val : Any
        a node value
    next : Optional [ ListNode ]
        pointer to next node in a list
    DEFAULT_VAL : Any
        a default node value to destinguish helper nodes

    Methods
    -------
    lst2linklst ( lst )
        A class method that returns class objects
        similar to constructor but for different use case -
        create linked list from list
    __init__ ( val, next )
        A 'constructor' of one node
    __str__ ( )
        A helper for print function
    """
    DEFAULT_VAL = -69
    @classmethod
    def lst2linklst(cls : ListNode, lst : List) -> ListNode:
        """
        Create linked list from list.

        :param lst List [ Any ]: python list of elements
        :return: linked list data structure
        :rtype: ListNode
        """
        if  not lst:
            return None
        cur = dummy = ListNode(ListNode.DEFAULT_VAL)
        for el in lst:
            cur.next = ListNode(el)
            cur = cur.next
        return dummy.next
    def __init__(self, val=0, next=None):
        """
        Initializes a ListNode object


        :param val Any: node value, default 0
        :param next Optional [ ListNode ]: next node default None
        :return: linked list data structure
        :rtype: ListNode
        """
        self.val = val
        self.next = next
    def __str__(self):
        """
        Generates  a string to be used py print function.

        :return: symulation of list elements
        :rtype: String
        """
        res = f'{str(self.val)}, '
        dummy = self.next
        while dummy:
            res += f'{str(dummy.val)}, '
            dummy = dummy.next
        res = res.strip(', ')
        return f'[{res}]'


if __name__ == '__main__':

    al1 = ListNode(1)
    a = ListNode(2)
    al1.next = a
    a = ListNode(3)
    al1.next.next = a
    a = ListNode(4)
    al1.next.next.next = a
    print(al1)

    al2 = ListNode.lst2linklst([1,2,3,4,5])
    print(al2)

    print(ListNode.lst2linklst([]))