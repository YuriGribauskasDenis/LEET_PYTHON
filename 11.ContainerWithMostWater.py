# 11.ContainerWithMostWater.py
def maxArea(height):
    l = 0
    r = len(height) - 1
    maxArea = -1
    while l != r:
        side01 = r - l
        if height[l] < height[r]:
            side02 = height[l]
            l += 1
        else:
            side02 = height[r]
            r -= 1
        curArea = side01 * side02
        if maxArea < curArea:
            maxArea = curArea
    return maxArea


print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1