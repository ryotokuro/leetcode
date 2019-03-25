# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# EXAMPLE
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.


def longestPalindromicSubString(string):
    # make a copy of string reversed

    reverse = reversed(string)

    # compare reverseString with string for longest
    for i in range(len(string)):
        if string[i] not in window:
            window[string[i]] += 1
            print(window)

        else:


    return


string = str(input())
print(longestPalindromicSubString(string))
