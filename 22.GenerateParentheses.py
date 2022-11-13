# 22.GenerateParentheses.py
def generateParenthesis(n):
    stack = []
    res = []

    def recursiveConstructor(openCount, closCount):
        if openCount == closCount ==n:
            res.append(''.join(stack))
            return

        if openCount < n:
            stack.append('(')
            recursiveConstructor(openCount + 1, closCount)
            stack.pop()

        if closCount < openCount:
            stack.append(')')
            recursiveConstructor(openCount, closCount + 1)
            stack.pop()

    recursiveConstructor(0, 0)

    return res


print(generateParenthesis(3))
# ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(2))
# ["(())", "()()"]
print(generateParenthesis(1))
# ["()"]