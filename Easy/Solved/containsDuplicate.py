# link: https://leetcode.com/problems/contains-duplicate/

# PROBLEM
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

# EXAMPLE
# Input: [1,2,3,1]
# Output: True

# EXAMPLE 2
# Input: [1,2,3,4]
# Output: False

# EXAMPLE 3
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: True


def containsDuplicate(arr):
    # O(n): Using Dictionary (140ms)
    seen = {}

    for i in arr:
        if i not in seen:
            seen[i] = 1
        else:
            return True
    return False


print(containsDuplicate([1, 2, 3, 1]))  # True
print(containsDuplicate([1, 2, 3, 4]))  # False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
