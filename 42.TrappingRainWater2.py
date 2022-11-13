# 42.TrappingRainWater.py
def trap(heights):
    n = len(heights)
    left = 0
    right = n - 1
    max_left = heights[0]
    max_right = heights[n - 1]
    res = 0
    while left < right:
        max_left = max(max_left, heights[left])
        max_right = max(max_right, heights[right])
        if max_left < max_right:
            res += max_left - heights[left]
            left += 1
        else:
            res += max_right - heights[right]
            right -= 1
    return res


print(trap([1,4,3,2,5])) # 3
print(trap([4,2,0,3,5,1])) # 7
print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9