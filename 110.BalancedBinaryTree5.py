# 110.BalancedBinaryTree.py
from leetcodelib import TreeNode

def isBalanced(root):
    if not root:
        return True

    def height(root):
        if not root:
            return 0
        return 1 + max(height(root.left), height(root.right))

    return (abs(height(root.left) - height(root.right)) < 2 and
        isBalanced(root.left) and isBalanced(root.right))


root = [3,9,20,None,None,15,7]
print(isBalanced(TreeNode.treefy(root))) # true

root = [1,2,2,3,3,None,None,4,4]
print(isBalanced(TreeNode.treefy(root))) # false