# 108.ConvertSortedArrayToBinarySearchTree.py
from leetcodelib import TreeNode

def sortedArrayToBST(nums):

    def helper(left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root

    return helper(0, len(nums) - 1)


print(sortedArrayToBST([-10,-3,0,5,9]))
# [0,-3,9,-10,null,5]
# [0,-10,5,null,-3,null,9] is also accepted:

print(sortedArrayToBST([1,3]))
# [3,1]
# [1,null,3] and [3,1] are both height-balanced BSTs.