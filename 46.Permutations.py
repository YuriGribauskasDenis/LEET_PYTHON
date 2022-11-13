# 46.Permutations.py
def permute(nums):
    res = []
    if  len(nums) == 1:
        return [nums[:]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

print(permute([1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute([0,1]))
# [[0,1],[1,0]]
print(permute([1]))
# [[1]]