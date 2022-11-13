# 42.TrappingRainWater.py
def trap(height):
    left = 1
    right = len(height) - 2
    max_left = height[0]
    max_right = height[len(height) - 1]
    trappedWater = 0
    while left <= right:
        if max_left < max_right:
            if height[left] < max_left:
                trappedWater += max_left - height[left]
            else:
                max_left = height[left]
            left += 1
        else:
            if height[right] < max_right:
                trappedWater += max_right - height[right]
            else:
                max_right = height[right]
            right -= 1
    return trappedWater


print(trap([1,4,3,2,5])) # 3
print(trap([4,2,0,3,5,1])) # 7
print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9