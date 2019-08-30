# link: https://leetcode.com/problems/implement-strstr/

# PROBLEM
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string?
# This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().


def strStr(haystack, needle):
    # empty string
    if not needle:
        return 0
    elif needle not in haystack:
        return -1
    else:
        i = 0
        while i < len(haystack):
            if haystack[i:i+len(needle)] == needle:
                return i
            i += 1

    # This is extremely trivial using built-in methods :(
    # Not what I'd want as an interviewer sooooooo
    # else:
    #     return haystack.find(needle)


print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))
