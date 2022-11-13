# 4.MedianOfTwoSortedArrays.py
def findMedianSortedArrays(nums1, nums2):
    INF = 2**31 - 1
    total = len(nums1) + len(nums2)
    half = total // 2
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1
    left = 0
    right = len(nums1) - 1
    while True:
        mid1 = left + ((right - left) // 2)
        mid2 = half - mid1 - 2
        nums1left = nums1[mid1] if mid1 >= 0 else -INF
        nums1right = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else INF
        nums2left = nums2[mid2] if mid2 >= 0 else -INF
        nums2right = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else INF
        # nums1left = nums1[mid1] if mid1 >= 0 else float('-infinity')
        # nums1right = nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float('infinity')
        # nums2left = nums2[mid2] if mid2 >= 0 else float('-infinity')
        # nums2right = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float('infinity')
        if nums1left <= nums2right and nums2left <= nums1right:
            if total % 2:
                return min(nums1right, nums2right)
            else:
                return (max(nums1left, nums2left) + min(nums1right, nums2right)) / 2
        elif nums1left > nums2right:
            right = mid1 - 1
        else:
            left = mid1 + 1


print(findMedianSortedArrays([1,3], [2])) # 2.0
print(findMedianSortedArrays([1,2], [3,4])) # 2.5