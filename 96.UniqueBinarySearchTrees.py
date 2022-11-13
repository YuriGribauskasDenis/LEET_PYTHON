# 96.UniqueBinarySearchTrees.py
from leetcodelib import TreeNode

def numTrees(n):
    # numTrees[4] = numTrees[0] * numTrees[3] +
    #               numTrees[1] * numTrees[2] +
    #               numTrees[2] * numTrees[1] +
    #               numTrees[3] * numTrees[0]
    # cache
    tab = [1] * (n + 1)
    # 0 nodes 1 tree
    # 1 nodes 1 tree
    for nodes in range(2, n + 1): # int
        total = 0
        for root in range(1, nodes + 1): # int
            left = root - 1
            right = nodes - root
            total += tab[left] * tab[right]
        tab[nodes] = total
    return tab[n]

print(numTrees(3)) # 5
print(numTrees(2)) # 2
print(numTrees(1)) # 1