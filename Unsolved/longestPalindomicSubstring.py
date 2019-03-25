# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# EXAMPLE
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.


def longestPalindromicSubString(string):
    # make a copy of string reversed
    stringIndexes = dict()
    reversedString = reversed(string)
    print(reversedString)

    # compare reversedString with string for longest substring
    for i in range(len(string)):
        if string[i] == reversedString[i]:
            stringIndexes[string[i]] = 1

    return "yes"


string = str(input())
print(longestPalindromicSubString(string))
