# link: https://leetcode.com/problems/move-zeroes/

# PROBLEM
# Given an array nums,
# write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# EXAMPLE
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# NOTE
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


def moveZeros(nums):  # function parameter is a list of ints
    print(nums)  # TESTING: to see how it looks before
    if 0 not in nums:  # don't waste time going through if no 0s
        return  # exit early always

    i = 0
    end = len(nums)
    print(end)
    while i < end:
        if nums[i] == 0:
            print(nums[i])
            del nums[i]  # del is a LOT faster than nums.remove() because remove() need to look for the zero
            nums.append(0)
            end -= 1
        else:
            i += 1

    # # SLOWER (200ms)
    #
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         nums.remove(0)
    #         nums.append(0)
    #     i += 1

    # # FASTER (168ms)
    # zeroCount = 0
    # while 0 in nums:
    #     zeroCount += 1
    #     nums.remove(0)
    #
    # z = [0] * zeroCount
    # nums.extend(z)

    # AFTER
    print(nums)
    return None


# nums = map(int, input().split(' '))
# moveZeros([0, 1, 0, 3, 12])
moveZeros([0, 0, 1])
