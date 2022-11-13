# 110.BalancedBinaryTree.py
from leetcodelib import TreeNode

def isBalanced(root):
    # naive, dfs left and right for every single node

    INF = 2**31 - 1

    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left) + 1
        right = dfs(root.right) + 1
        if abs(left - right) > 1:
            return INF
        return max(left, right)

    return dfs(root) != INF


root = [3,9,20,None,None,15,7]
print(isBalanced(TreeNode.treefy(root))) # true

root = [1,2,2,3,3,None,None,4,4]
print(isBalanced(TreeNode.treefy(root))) # false