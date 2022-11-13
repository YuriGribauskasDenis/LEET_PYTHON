# 94.BinaryTreeInorderTraversal.py
from leetcodelib import TreeNode

# recursive
def inorderTraversal(root):
    res = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    
    inorder(root)
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