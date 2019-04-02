# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# EXAMPLE
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.


def longestPalindromicSubString(string):
    # make a copy of string reversed
    stringIndexes = dict()

    i = 0
    j = len(string)
    print(string[i:j])
    print(string[i:j][::-1])  # [::-1] is the reverse slicing
    # compare reversedString with string for longest substring

    return "yes"


string = str(input())
print(longestPalindromicSubString(string))
