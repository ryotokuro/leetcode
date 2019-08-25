# link:

# PROBLEM
# Given two strings s and t , write a function to determine if t is an anagram of s.

# EXAMPLE
# Input: s = "anagram", t = "nagaram"
# Output: True

# EXAMPLE 2
# Input: s = "rat", t = "car"
# Output: False

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


def validAnagram(s, t):
    print()
    print(s, t)  # self-testing purposes

    # EDGE CASES
    # Okay first I need to make sure they're the same LENGTH
    if len(s) != len(t):
        return False
    # If its empty then return True? I guess
    if s == t == '':
        return True

    # So from here we know that they're both the same length and non-empty
    # USING A DICTIONARY TO COMPARE LETTER FREQUENCIES
    # sorting is a bottleneck so lets remove that
    # simply store count of letters in each string in a dict
    # constant lookup so we can just compare dicts
    s_chars = {}
    t_chars = {}
    for i in s:
        s_chars[i] = s_chars.get(i, 0) + 1

    for j in t:
        t_chars[j] = s_chars.get(j, 0) + 1
    print(s_chars, t_chars, sep='\n')
    return s_chars == t_chars

    # SLOW (80ms, O(nlogn) solution due to timsort (worst case))
    # s = list(s)
    # s.sort()
    # t = list(t)
    # t.sort()
    #
    # i = 0
    # while i < len(s):
    #     if s[i] != t[i]:
    #         return False
    #     i += 1
    #
    # return True


# s, t = input().split(' ')
print(validAnagram('anagram', 'nagaram'))  # True
print(validAnagram('rat', 'car'))  # False
print(validAnagram('a', 'a'))  # False
