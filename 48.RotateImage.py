# 48.RotateImage.py
def rotate(matrix):
    left = 0
    right = len(matrix[0]) - 1
    while left < right:
        # for i in range(left, right - 1):
        for i in range(right - left):
            top = left
            bottom = right

            topLeft = matrix[top][left+i]
            matrix[top][left+i] = matrix[bottom-i][left]
            matrix[bottom-i][left] = matrix[bottom][right-i]
            matrix[bottom][right-i] = matrix[top+i][right]
            matrix[top+i][right] = topLeft
        right -= 1
        left += 1
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#[[7,4,1],[8,5,2],[9,6,3]]
print(rotate(matrix))

matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
    ]
# [
    # [15,13,2,5],
    # [14,3,4,1],
    # [12,6,8,9],
    # [16,7,10,11]
    # ]
print(rotate(matrix))