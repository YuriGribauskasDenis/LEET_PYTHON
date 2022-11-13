# 110.BalancedBinaryTree.py
from leetcodelib import TreeNode

# DFS: find each subtree's depth, and compare the two.
# However, making DFS for every node is very costly: the recursive calculations of depth are done repeatedly, so we want to at least tell, if a path has failed, no need to dive deep -> need a boolean-ish signature. 
# However, we can't return both boolean && depth (we actually don't need other depth valuese greater than 1).
# Combine the boolean && depth signature to mark the failed case: by using a negative number.

def isBalanced(root):
    if not root:
        return True
    MINVAL = float('-inf')
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return MINVAL
        return 1 + max(dfs(root.left), dfs(root.right))

    return dfs(root) > 0


root = [3,9,20,None,None,15,7]
print(isBalanced(TreeNode.treefy(root))) # true

root = [1,2,2,3,3,None,None,4,4]
print(isBalanced(TreeNode.treefy(root))) # false