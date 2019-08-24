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
    print(s, t)  # self-testing purposes

    # EDGE CASES
    # Okay first I need to make sure they're the same LENGTH
    if len(s) != len(t):
        return False
    # If its empty then return True? I guess
    if s == t == '':
        return True

    # So from here we know that they're both the same length and non-empty
    s = list(s)
    s.sort()
    t = list(t)
    t.sort()

    i = 0
    while i < len(s):
        if s[i] != t[i]:
            return False
        i += 1

    return True


# s, t = input().split(' ')
print(validAnagram('anagram', 'nagaram'))  # True
print(validAnagram('rat', 'car'))  # False
