# 42.TrappingRainWater.py
def trap(heights):
    n = len(heights)
    left = 0
    right = n - 1
    max_left = 0
    max_right = 0
    res = 0
    while left < right:
        if heights[left] < heights[right]:
            if max_left < heights[left]:
                max_left = heights[left]
            else:
                res += max_left - heights[left]
            left += 1
        else:
            if max_right < heights[right]:
                max_right = heights[right]
            else:
                res += max_right - heights[right]
            right -= 1
    return res


print(trap([1,4,3,2,5])) # 3
print(trap([4,2,0,3,5,1])) # 7
print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9