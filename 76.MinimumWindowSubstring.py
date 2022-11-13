# 76.MinimumWindowSubstring.py
def minWindow(s, t):
    if t =='':
        return ''
    window = {}
    countT = {}
    for c in t:
        countT[c] = countT.get(c, 0) + 1
    have = 0
    need = len(countT)

    # float('infinity')
    INFINITY = 2**63 - 1
    res = [-1, -1]
    resLen = INFINITY
    left = 0

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1

        if c in countT and window[c] == countT[c]:
            have += 1
        
        while have == need:
            if right - left + 1 < resLen:
                resLen = right - left + 1
                res = [left, right]
            window[s[left]] -= 1
            if s[left] in countT and window[s[left]] < countT[s[left]]:
                have -= 1
            left += 1
    left, right = res        
    return s[left : right + 1] if resLen != INFINITY else ''


print(minWindow('ADOBECODEBANC', 'ABC')) #'BANC'
print(minWindow('a', 'a')) #'a'
print(minWindow('a', 'aa')) #''