# 110.BalancedBinaryTree.py
from leetcodelib import TreeNode


def isBalanced(root):
    # botom up recursively
    def dfs(root):
        if root is None:
            return True, 0
        left = dfs(root.left)
        right = dfs(root.right)
        balance = abs(left[1] - right[1])
        balanced = left[0] and right[0] and balance <= 1
        return balanced, 1 + max(left[1], right[1])
    return dfs(root)[0]


root = [3,9,20,None,None,15,7]
print(isBalanced(TreeNode.treefy(root))) # true

root = [1,2,2,3,3,None,None,4,4]
print(isBalanced(TreeNode.treefy(root))) # false