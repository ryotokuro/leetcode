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
    # in the case of an empty string
    if len(string) == 1:
        return 1

    longest, substring = "", ""

    # check letter doesn't already exist in the substring
    # e.g. if('a' not in substring)
    for i in range(len(string)):
        # might need two for loops and run through two instances of the loop
        for j in range(i+1, len(string)):
        # if not in the substring then append
        if string[i] not in substring:
            substring += (string[i])
        # else (it is in the substring = repeating character)
        else:
            # compare with longest and store
            # set longest to max(len(substring), len(longest))
            if len(substring) > len(longest):
                longest = substring

            # start new substring
            substring = string[i]

    if len(substring) > len(longest):
        longest = substring

    return len(longest)


# SETUP INPUT METHOD
string = str(input("Input: "))
print("Output:", longestSubstring(string))
# print("Explanation: The answer is " + longest, "with the length of", maxLen)
