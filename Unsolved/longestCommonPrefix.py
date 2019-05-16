# PROBLEM
# Write a function to find the longest common prefix string amongst an array of strings.
# Edge Case: If there is no common prefix, return an empty string "".
# Note: All inputs are in lowercase letters a-z


def longestCommonPrefix(strings):
        # to avoid overflow, want to use the length of the smallest word in the list
        commonPrefix = ""

        if len(strings) == 1:
            return strings[0]

        if strings != []:
            shortLen = min(strings, key=len)
            finished = False

            # procedurally need to compare letters
            for i in range(1, len(shortLen)):
                testPrefix = strings[0][:i]

                for j in range(1, len(strings)):
                    if strings[j][:i] != testPrefix:  # if any one of the strings dont match
                        finished = True  # trigger mismatch flag
                        break  # exit loop early to save time

                if finished:
                    break

                else:
                    commonPrefix = strings[0][:i]

        return commonPrefix  # return longest common prefix using first element in the list


# TESTS
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
print("heck" + longestCommonPrefix([]))
