# treelib.py
from collections import deque
class TreeNode:

    @classmethod
    def treefy(cls, lst):
        # if lst == [] or lst == None:
        if not lst:
            return None
        n = len(lst)
        trist = []
        for el in lst:
            if el is not None:
                trist.append(TreeNode(el))
            else:
                trist.append(None)
        for i in range(len(lst)):
            i1 = 2*i+1
            if lst[i] and i1 < n:
                trist[i].left = trist[i1]
            i2 = 2*i+2
            if lst[i] and i2 < n:
                trist[i].right = trist[i2]
        return(trist[0])

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        res = []
        queue = deque([(self, 0)])
        count = 0
        while queue:
            curr_node, i = queue.popleft()
            if curr_node is None:
                res.append(None)
                count += 1
                continue

            for _ in range(i - count):
                res.append(None)
            res.append(curr_node.val)
            count += i - count + 1

            queue.append((curr_node.left, 2*i + 1))
            queue.append((curr_node.right,2*i + 2))
        while res[-1] is None:
            res.pop()
        res = list(map(str, res))
        res = ', '.join(res)
        return f'[{res}]'


if __name__ == '__main__':
    t3 = TreeNode(3)
    t3.left = TreeNode(9)
    t3.right = TreeNode(20)
    t3.right.left = TreeNode(15)
    t3.right.right = TreeNode(7)
    print(t3)
    t3_02 = TreeNode.treefy([3, 9, 20, None, None, 15, 7])
    print(t3_02)

    print(TreeNode.treefy([]))

    print('='*50)
    t3_03 = TreeNode.treefy([1,2,3,None,5,None,4,None,None,7,8,None, None,9])
    print(t3_03)
    print('='*50)

    tr3 = TreeNode(1)
    tr3.left = TreeNode(2)
    tr3.right = TreeNode(3)
    tr3.left.right = TreeNode(5)
    tr3.right.right = TreeNode(4)
    tr3.left.right.left  = TreeNode(7)
    print(tr3)


    t3_0k = TreeNode.treefy([3,1,4,None,2])
    print(t3_0k)