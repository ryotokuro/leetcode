# PROBLEM
# Given:
# - an array of integers

# Return:
# - indices of the two numbers such that they add up to a SPECIFIC target.

# Assume:
# - each input would have exactly one solution, and you may not use the same element twice.

# EXAMPLE
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(nums):
            for j in range(nums)

            if == target:
                low = i
                high = j

        return list(low, high)