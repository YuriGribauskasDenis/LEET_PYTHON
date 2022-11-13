# 3.LongestSubstringWithoutRepeatingCharacters.py
# slicing window
# two pointers
def lengthOfLongestSubstring(s):
    left = 0
    charSet = set()
    max_len = 1
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


print(lengthOfLongestSubstring('bbbbb')) #1
print(lengthOfLongestSubstring('pwwkew')) #3
print(lengthOfLongestSubstring('abcabcbb')) #3
print(lengthOfLongestSubstring('abccbcfbb')) #3