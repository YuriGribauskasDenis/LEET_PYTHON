# 11.ContainerWithMostWater.py
def maxArea(height):
    l = 0
    r = len(height) - 1
    maxArea = 0
    while l < r:
        curArea = min(height[l], height[r]) * (r - l)
        maxArea = max(maxArea, curArea)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxArea


print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1