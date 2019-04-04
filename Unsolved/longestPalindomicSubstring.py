# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# EXAMPLE
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# OWN EXAMPLE - sliding window
sfdobabado 9
j-1

sfdobabad 0 to 8
or
fdobabado 1 to 9

j-1

sfdobaba 0 to 7
fdobabad 1 to 8
dobabado 2 to 9

j-1

sfdobab
fdobaba
dobabad
obabado

j-1

sfdoba
fdobab
dobaba
obabad
babado

j-1

sfdob
fdoba
dobab
obaba
babad
abado

j-1

sfdo
fdob
doba
obab
baba
abad
bado

j-1

sfd
fdo
dob
oba
bab STOP

def longestPalindromicSubString(string):
    # make a copy of string reversed
    stringIndexes = dict()

    j = len(string)
    gap = 0
    for i in range(len(string)):
        # window is i to j length
            
        if string[i:j] == string[i:j][::-1]: # print(string[i:j][::-1])  # [::-1] is the reverse slicing
            break # we go from the biggest combinations, so the first encounter is the biggest


    return string[i:j]


string = str(input())
print(longestPalindromicSubString(string))
