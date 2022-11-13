# 84.LargestRectangleInHistogram.py
def largestRectangleArea(heights):
    maxArea = 0
    stack = [] # (index, heights)

    for i in range(len(heights)):
        start = i
        while stack and stack[-1][1] > heights[i]:
            index, h = stack.pop()
            maxArea = max(maxArea, h * (i - index))
            start = index
        stack.append((start, heights[i]))
    
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    
    return maxArea


print(largestRectangleArea([2,4])) # 4
print(largestRectangleArea([2,1,5,6,2,3])) # 10
print(largestRectangleArea([2,1,2])) # 3