# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# EXAMPLE
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# OWN EXAMPLE - sliding window
# sfdobabado 9
# j-1
#
# sfdobabad 0 to 8
# or
# fdobabado 1 to 9
#
# j-1
#
# sfdobaba 0 to 7
# fdobabad 1 to 8
# dobabado 2 to 9
#
# j-1
#
# sfdobab
# fdobaba
# dobabad
# obabado
#
# j-1
#
# sfdoba
# fdobab
# dobaba
# obabad
# babado
#
# j-1
#
# sfdob
# fdoba
# dobab
# obaba
# babad
# abado
#
# j-1
#
# sfdo
# fdob
# doba
# obab
# baba
# abad
# bado
#
# j-1
#
# sfd
# fdo
# dob
# oba
# bab STOP


def longestPalindromicSubString(string):
    # initial values
    gap = i = 1  # keeps track of increasing difference
    j = len(string)  # set j as the end boundary
    done = False  # done will determine whether we have found a match or not

    while i != j:
        if string[i:j] != string[i:j][::-1]:  # if the string window matches its reverse
            j -= 1
            gap += 1
            for k in range(gap):  # from 0 to gap
                # print("i+k", i+k)
                # print(string[i+k:j+k] == string[i+k:j+k][::-1])  # i and j move along according to k
                if string[i+k:j+k] == string[i+k:j+k][::-1]:  # [::-1] is the reverse slicing
                    i += k  # save variables in case it works
                    j += k
                    done = True
                    break  # we go from the biggest combinations, so the first encounter is the biggest
            if done:
                break
        else:  # the original string is the biggest palindrome
            break

    return string[i:j]


string = str(input())
print(longestPalindromicSubString(string))
