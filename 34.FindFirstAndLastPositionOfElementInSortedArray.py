# 34.FindFirstAndLastPositionOfElementInSortedArray.py
def searchRange(nums, target):
    def binSearch(nums, target, leftSearch):
        left = 0
        right = len(nums) - 1
        res = -1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                res = mid
                if leftSearch:
                    right = mid - 1
                else:
                    left = mid + 1
        return res
    left_res = binSearch(nums, target, True)
    right_res = binSearch(nums, target, False)
    return left_res, right_res


print(searchRange([5,7,7,8,8,10], 8)) # [3, 4]
print(searchRange([5,7,7,8,8,10], 6)) # [-1, -1]
print(searchRange([], 0)) # [-1, -1]