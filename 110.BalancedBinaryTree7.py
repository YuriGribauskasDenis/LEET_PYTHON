# 110.BalancedBinaryTree.py
from leetcodelib import TreeNode

# Recursive
# Calculate a node's maxDepth - height.
# Compare a parent node's sub tree for maxDepth
def isBalanced(root):
    def height(root):
        return (max(height(root.left), height(root.right)) + 1
            if root else 0)
    if not root:
        return True
    left = height(root.left)
    right = height(root.right)
    if abs(left - right) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right);


root = [3,9,20,None,None,15,7]
print(isBalanced(TreeNode.treefy(root))) # true

root = [1,2,2,3,3,None,None,4,4]
print(isBalanced(TreeNode.treefy(root))) # false