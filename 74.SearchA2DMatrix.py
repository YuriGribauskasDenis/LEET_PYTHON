# 74.SearchA2DMatrix.py
def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    top = 0
    bot = ROWS - 1
    while top <= bot:
        mid_row = bot + ((top - bot) // 2)
        if matrix[mid_row][-1] < target: # COLS-1
            top = mid_row + 1
        elif target < matrix[mid_row][0]:
            bot = mid_row - 1
        else:
            break
    if not top <= bot:
        return False
    left = 0
    right = COLS - 1
    while left <= right:
        mid_col = left + ((right - left) // 2)
        if matrix[mid_row][mid_col] < target:
            left = mid_col + 1
        elif target < matrix[mid_row][mid_col]:
            right = mid_col - 1
        else:
            return True
    return False


matrix = [
        [ 1, 3, 5, 7],
        [10,11,16,20],
        [23,30,34,60]
        ]
print(searchMatrix(matrix, 3))  # true
print(searchMatrix(matrix, 13)) # false