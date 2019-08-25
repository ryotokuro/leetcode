# link: https://leetcode.com/problems/valid-anagram/

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
    print(s, t)  # self-testing purposes

    # EDGE CASES
    # Okay first I need to make sure they're the same LENGTH
    if len(s) != len(t):
        return False
    # If its empty then return True? I guess
    if s == t == '':
        return True
    # So from here we know that they're both the same length and non-empty

    # HASH-MAP TO COMPARE LETTER FREQUENCIES (64ms)
    # Sorting is a bottleneck that runs O(nlogn) so we remove it
    # Simply store count of letters in each string in a dict
    s_chars = {}  # create a dictionary for ss
    t_chars = {}  # and a separate one (needs to be on different lines)
    for i in s:
        s_chars[i] = s_chars.get(i, 0) + 1  # if not in dict, set to 1

    for j in t:  # do the same for string t
        t_chars[j] = t_chars.get(j, 0) + 1

    print(s_chars, t_chars, sep='\n')
    return s_chars == t_chars  # now we can simply compare and see if they hold the same letters :)

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


# TEST CASES
print(validAnagram('anagram', 'nagaram'))  # True
print()
print(validAnagram('rat', 'car'))  # False
print()
print(validAnagram('a', 'b'))  # False
