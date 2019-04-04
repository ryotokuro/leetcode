# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# EXAMPLE
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# OWN EXAMPLE - sliding window
sfdobabado
j-1

sfdobabad
or
fdobabado

j-1

sfdobaba
fdobabad
dobabado

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

    for i in range(len(string)):
    j = len(string)

    print(string[i:j])
    print(string[i:j][::-1])  # [::-1] is the reverse slicing
    # compare reversedString with string for longest substring

    return "yes"


string = str(input())
print(longestPalindromicSubString(string))
