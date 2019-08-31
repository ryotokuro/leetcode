# link: https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums,
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.


def maxSubArray(nums):
    # empty list
    if not nums:
        return 0

    # O(nlogn) solution (using sorting)
    if sorted(nums)[-1] <= 0:
        return sorted(nums)[-1]
    elif sorted(nums)[0] >= 0:
        return sum(nums)

    # maybe i can go through it once and find the min and max values
    # then when comparing sums, i check if it ever exceeds the max or drops below the min
    most = nums[0]
    for i in nums:
        most = max(i, most)

    # now the var most has the largest value in the list
    # might have to use kadane's algorithm from this point?
    # https://www.youtube.com/watch?v=86CQq3pKSUw

    # optimisation problem (need to check through O(n^2)...

    # and then try divide/conquer
    for index, value in enumerate(nums):
        if value >= 0:
            break
    print(nums[index:len(nums)+1])
    return sum(nums[index:len(nums)+1])


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([3, 6, 21, 1, 43, 0, 21]))
