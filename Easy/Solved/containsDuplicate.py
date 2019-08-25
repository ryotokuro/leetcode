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
    # GENIUS solution, using a list comparison
    # Makes this trivial in Python
    # return len(arr) > len(set(arr))  # One-line but its slower (144ms)

    # Since I don't actually need the value in the key-value a dict provides
    # It'd be more useful to use a hash-set which will use less memory
    # O(n): Using Hash-set (136ms)
    count = set()
    for i in arr:
        if i not in count:
            count.add(i)
        else:
            return True
    return False

    # # O(n): Using Dictionary (140ms)
    # seen = {}
    #
    # for i in arr:
    #     if i not in seen:
    #         seen[i] = 1
    #     else:
    #         return True
    # return False


print(containsDuplicate([1, 2, 3, 1]))  # True
print(containsDuplicate([1, 2, 3, 4]))  # False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
