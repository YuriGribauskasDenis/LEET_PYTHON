# 33.SearchInRotatedSortedArray.py
def search(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = left + ((right - left) // 2)
        if nums[mid] == target:
            return mid
        # left sorted portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


print(search([4,5,6,7,0,1,2], 0)) # 4
print(search([4,5,6,7,0,1,2], 3)) # -1
print(search([1], 0)) # -1