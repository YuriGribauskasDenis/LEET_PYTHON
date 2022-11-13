# 1.TwoSum.py
def twoSum(nums, target):
    num2idx = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in num2idx:
            return i, num2idx[x]
        num2idx[nums[i]] = i


print(twoSum([2,7,11,15], 9)) #[0,1]
print(twoSum([3,2,4], 6)) #[1,2]
print(twoSum([3,3], 6)) #[0,1]