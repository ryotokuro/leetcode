# EXAMPLE 1
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# EXAMPLE 2
# Input: "dvdf"
# Output: 3
# Explanation: The answer is "vdf", with the length of 3.

# PLAN
# Consider substrings CASE by CASE
# If repeated character, start new current count, store max count
# At the end, compare maxCount with the current count

# WHAT I NEED
# substring - tracks current substring
# longest - stores the longest substring

# OPTIONAL
# index - keep track of index :)


def longestSubstring(string):
    # in the case of an empty string
    if len(string) == 1:
        return 1

    longest = ""
    # idea: create a SLIDING window
    window = dict()

    # initially the bounds of the window is i, j (where j = i intially)

    # check if j exists in the window
    # if not, then we extend, and slide the window further
    i = j = 0
    while i < len(string):
        if string[j] not in window:
            window[string[j]] = j  # store position so i can retrieve later?
            j += 1  # increment j

        # if it does, then we restart the window
        else:
            i += 1
            j = i

    return len(longest)


# SETUP INPUT METHOD
string = str(input("Input: "))
print("Output:", longestSubstring(string))
# print("Explanation: The answer is " + longest, "with the length of", maxLen)
