# link: https://leetcode.com/problems/majority-element/

# PROBLEM
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# EXAMPLE
# Input: [3,2,3]
# Output: 3


def majorityElement(nums):
    majority = len(nums) // 2
    occur = {}
    for i in nums:
        if i not in occur:
            occur[i] = 1
        else:
            occur[i] += 1

    # next check hashmap for highest value
    print(occur)
    for key, val in occur.items():
        if val > majority:
            majority = key
            break
    return majority


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
