# 20.ValidParentheses.py
def isValid(s):
    close2open = {')':'(',']':'[','}':'{'}
    stack = []
    for c in s:
        if c in close2open:
            if stack and stack[-1] == close2open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    # return True if not stack else False
    return not stack



print(isValid('()')) # true
print(isValid('()[]{}')) # true
print(isValid('(]')) # false