# 71.SimplifyPath.py
def simplifyPath(path):
    stack = []
    curr = ''
    for c in f'{path}/':
        if c == '/':
            if curr == '..':
                if stack: stack.pop()
            elif curr not in ['.', '']:
                stack.append(curr)
            curr = ''
        else:
            curr += c
    return '/' + '/'.join(stack)


print(simplifyPath('/../')) # '/'
print(simplifyPath('/home//foo/')) # '/home/foo'