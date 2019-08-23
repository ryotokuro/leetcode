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
    # BEFORE
    print(nums)

    

    # # SLOWER (200ms)
    # if 0 not in nums:
    #     return
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
moveZeros([0, 1, 0, 3, 12])
