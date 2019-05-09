# PROBLEM
# Write a function to find the longest common prefix string amongst an array of strings.
# Edge Case: If there is no common prefix, return an empty string "".
# Note: All inputs are in lowercase letters a-z

def longestCommonPrefix():
# to avoid overflow, want to use the length of the smallest word in the list


# TESTS
print(longestCommonPrefix(["flower","flow","flight"]))  # Output "fl"
print(longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
