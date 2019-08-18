# PROBLEM
# Write a function to find the longest common prefix string amongst an array of strings.
# Edge Case: If there is no common prefix, return an empty string "".
# Note: All inputs are in lowercase letters a-z


def longestCommonPrefix(strings):
        # if there is only one string in the array
        if len(strings) == 1:
            return strings[0]

        # else, there is more than one string in the array
        else:
            # if the list is empty, we want to return an empty string
            commonPrefix = ""
            # print(strings[1][:1], strings[0][:1], list(range(len(min(strings, key=len))+1)))
            # note: in python empty sequences are FALSE
            if strings:  # if the string is not empty (implicit boolean when string is empty)
                shortLen = min(strings, key=len)  # short the length of the shortest
                finished = False

                # procedurally need to compare letters
                for i in range(1, len(shortLen)+1):
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
print(longestCommonPrefix(["c", "c"]))                    # Output: "c"
#print("heck" + longestCommonPrefix([]))
