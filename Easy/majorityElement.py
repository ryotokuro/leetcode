# link: https://leetcode.com/problems/majority-element/

# PROBLEM
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# EXAMPLE
# Input: [3,2,3]
# Output: 3

# Interesting point, given that a majority element is ALWAYS present in the list,
# then the majority element will always be the MIDDLE element in the sorted list
# however in Python, this is not the most time-efficient since Python uses 'timsort'
# so on average the time complexity is O(logn) with worst case O(nlogn)


def majorityElement(nums):
    # MAJORITY VOTE ALGORITHM
    # Most efficient O(n) time and O(1) space
    # https://www.cs.utexas.edu/~moore/best-ideas/mjrty/
    majority = nums[0]
    count = 0
    for num in nums:
        if count == 0:
            majority = num
            count = 1
        elif num == majority:
            count += 1
        elif num != majority:
            count -= 1

    # majority = len(nums) // 2
    # occur = {}
    # for i in nums:
    #     if i not in occur:
    #         occur[i] = 1
    #     else:
    #         occur[i] += 1
    #
    # # next check hashmap for highest value
    # print(occur)
    # for key, val in occur.items():
    #     if val > majority:
    #         majority = key
    #         break
    return majority


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
