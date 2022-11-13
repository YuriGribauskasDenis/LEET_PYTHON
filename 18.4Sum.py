# 18.4Sum.py
def fourSum(nums, target):
    res = []
    nums.sort()
    quad = []
    def kSum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if start < i and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()
            return
        #base case two sum
        left = start
        right = len(nums) - 1
        while left < right:
            twoSum = nums[left] + nums[right]
            if twoSum < target:
                left += 1
            elif target < twoSum:
                right -= 1
            else:
                res.append(quad + [nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    kSum(4, 0, target)
    return res


print(fourSum([1,0,-1,0,-2,2], 0))
# [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum([2,2,2,2,2], 8))
# [[2,2,2,2]]