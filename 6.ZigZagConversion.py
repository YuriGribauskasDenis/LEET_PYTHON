# 6.ZigZagConversion.py
def convert(s, numRows):
    if numRows == 1:
        return s
    res = ''
    increment = 2 * (numRows - 1)
    for r in range(numRows):
        for j in range(r, len(s), increment):
            res += s[j]
            if r > 0 and r < numRows - 1 and j + increment - 2 * r < len(s):
            # if (0 < r and r < numRows - 1 and
            #     j + increment - 2 * r < len(s)):
                res += s[j + increment - 2 * r]
    return res


print(convert('PAYPALISHIRING', 3)) #"PAHNAPLSIIGYIR"
print(convert('PAYPALISHIRING', 4)) #"PINALSIGYAHRPI"
print(convert('A', 1)) #"A"