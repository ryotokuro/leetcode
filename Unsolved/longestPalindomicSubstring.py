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
    start = end = i = j = 0  # keeps track of increasing difference
    done = False

    while i != j:
        # window is from i to j (length)
        if string[i:j] != string[i:j][::-1]:
            gap = 1
            for k in range(gap):
                print(string[i+k:j+k] == string[i+k:j+k][::-1])
                if string[i+k:j+k] == string[i+k:j+k][::-1]:  # print(string[i:j][::-1])  # [::-1] is the reverse slicing
                    start = i+k
                    end = j+k
                    done = True
                    break  # we go from the biggest combinations, so the first encounter is the biggest
            if done:
                break
        else:
            break
        gap += 1  # increase gap after each failed attempt

    return string[start:end]


string = str(input())
print(longestPalindromicSubString(string))
