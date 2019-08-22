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


def moveZeros(nums: list[int]):  # function parameter is a list of ints
    zeroCount = 0
    while 0 in nums:
        zeroCount += 1
        nums.remove(0)

    z = [0] * zeroCount
    nums.extend(z)
    return None


nums = map(int, input().split(' '))
moveZeros([0, 1, 0, 3, 12])
