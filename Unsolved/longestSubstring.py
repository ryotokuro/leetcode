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

    longest, substring = "", ""

    # idea: create a SLIDING window
    window = dict()

    # initially the bounds of the window is i, j (where j = i intially)

    # check if j exists in the window
    # if not, then we extend, and slide the window further
    if j not in window:
        continue
    # if it does, then we restart the window
    else:
        break
    # check letter doesn't already exist in the substring
    # e.g. if('a' not in substring)
    for i in range(len(string)):
        # start new substring
        substring = string[i]

        # might need two for loops and run through two instances of the loop
        for j in range(i+1, len(string)):
            # if not in the substring then append
            if string[j] not in substring:
                substring += (string[j])
            # else (it is in the substring = repeating character)
            else:
                # compare with longest and store
                if len(substring) > len(longest):
                    longest = substring  # set longest to max(len(substring), len(longest))

    if len(substring) > len(longest):
        longest = substring

    return len(longest)


# SETUP INPUT METHOD
string = str(input("Input: "))
print("Output:", longestSubstring(string))
# print("Explanation: The answer is " + longest, "with the length of", maxLen)
