# 94.BinaryTreeInorderTraversal.py
from leetcodelib import TreeNode


# iterative
def inorderTraversal(root):
    res = []
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right

    return res


# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

print(inorderTraversal(TreeNode.treefy([1,None,2,None,None,3]))) # [1,3,2]
print(inorderTraversal(TreeNode.treefy([]))) # []
print(inorderTraversal(TreeNode.treefy([1]))) # [1]

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right = TreeNode(5)

print(inorderTraversal(TreeNode.treefy([1,2,5,3,4]))) # [1,3,2]