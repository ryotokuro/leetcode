# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# PROBLEM
# Given a sorted array nums,
# remove the duplicates in-place such that each element appear only once and return the new length.
#
# NOTE
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.

# EXAMPLE
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.

# EXAMPLE 2
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5,
# with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.

# CLARIFICATION
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference,
# which means modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


def removeDuplicates(nums):
    # 116ms solution (quite slow, O(n))
    length = len(nums)

    # EDGE CASES
    if length == 0:
        return 0
    elif length == 1:
        return 1

    prev = 0
    curr = 1
    while curr < length:
        if nums[curr] == nums[prev]:
            del nums[curr]
            length -= 1
        else:
            prev = curr
            curr += 1
    print(nums)
    return length


print(removeDuplicates([1, 1, 2]))  # return length = 2
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # return length = 5
