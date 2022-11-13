# 3.LongestSubstringWithoutRepeatingCharacters.py
# smart straight foreward solution
def lengthOfLongestSubstring(s):
    max_len = 0
    cur_len = 0
    d = {}
    start = 0
    end = 0
    for i, c in enumerate(s):
        if c in d:
            start = max(start, d[c])
        cur_len = end - start + 1
        max_len = max(max_len, cur_len)
        d[c] = i + 1
        end += 1
        # print(f'{c} {s[start: end]}')
        # print(f'{start = } {end = } {cur_len = } {max_len = } {d = }')
        # print()
    return max_len


print(lengthOfLongestSubstring('bbbbb')) #1
print(lengthOfLongestSubstring('pwwkew')) #3
print(lengthOfLongestSubstring('abcabcbb')) #3
print(lengthOfLongestSubstring('abccbcfbb')) #3