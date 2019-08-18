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
# hash map to keep track of where things are
# longest store

# OPTIONAL
# index - keep track of index :)


def longestSubstring(string):
    # idea: create a SLIDING window
    window = dict()

    longest = i = j = 0  # initially the bounds of the window is i, j (where j = i intially)

    while i < len(string) and j < len(string):
        #print(string[j], string[j] not in window)
        if string[j] not in window:  # check if j exists in the window
            # if not, then we extend, and slide the window further
            window[string[j]] = j  # store position so i can retrieve later?
            j += 1  # increment j
            # print(window)

        else:  # if it does, then we reset the window
            if len(window) > longest:
                longest = len(window)
            # even if the length of the new window isn't the longest, we have to clear it
            window.clear()
            i = j
            j = i
            if longest > (len(string) - i):  # breaks early if the length of the longest substring > characters left
                print(i)
                break

    # ideally would like to break early if length is bigger
    if len(window) > longest:
        longest = len(window)
        window.clear()

    return longest


# SETUP INPUT METHOD
string = str(input("Input: "))
print("Output:", longestSubstring(string))
# print("Explanation: The answer is " + longest, "with the length of", maxLen)
