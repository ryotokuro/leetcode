# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# PLAN
# Consider substrings CASE by CASE
# If repeated character, start new current count, store max count
# At the end, compare maxCount with the current count

# WHAT I NEED
# currLen - tracks count of the case
# maxLen - length of biggest substring
# longest - stores the longest substring

# OPTIONAL
# substring - tracks current substring (not necessary but only for print purpose)
# index - keep track of index :)
def longestSubstring(string):
    currLen, maxLen = 0, 0
    longest, substring = "", ""

    # check letter doesn't already exist in the substring
    # e.g. if('a' not in substring)

    # if not in the substring then append

    # else (it is in the substring = repeating character)
    # compare with longest and store
    # set longest to max(len(substring), len(longest))

    # start new substring
    return maxLen


# SETUP INPUT METHOD
string = str(input("Input: "))
print("Output:", longestSubstring(string))
print("Explanation: The answer is " + longest, "with the length of", maxLen)
