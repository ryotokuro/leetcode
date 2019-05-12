# PROBLEM
# Write a function to find the longest common prefix string amongst an array of strings.
# Edge Case: If there is no common prefix, return an empty string "".
# Note: All inputs are in lowercase letters a-z

def longestCommonPrefix(strings):
    # to avoid overflow, want to use the length of the smallest word in the list
    shortLen = min(strings, key=len)
    testPrefix = commonPrefix = ""

    # procedurally need to compare letters
    for i in range(shortLen):
        testPrefix = strings[j][i]
        for j in range(len(strings)):

            if strings[j][i] != testPrefix

    return strings[0[:shortLen]]  # return longest common prefix using first element in the list


# TESTS
print(longestCommonPrefix(["flower","flow","flight"]))  # Output "fl"
print(longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
