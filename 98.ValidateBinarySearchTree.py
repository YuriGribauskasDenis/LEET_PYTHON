# 98.ValidateBinarySearchTree.py
from treelib import TreeNode

# recursive dfs
def isValidBST(root):
    def helper(node, left, right):
        if not node:
            return True
        if not (left < node.val and node.val < right):
            return False
        
        return (helper(node.left, left, node.val) and
                helper(node.right, node.val, right))

    return helper(root, float('-inf'), float('inf'))


print(isValidBST(TreeNode.treefy([2,1,3]))) # true
print(isValidBST(TreeNode.treefy([5,1,4,None,None,3,6]))) # false