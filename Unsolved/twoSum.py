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
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Pseudo-example:
        # [1, 2, 3, 4]
        # Iteration of the loop goes:
        # - 12, 13, 14, 23, 24, 34

        for i in range(len(nums)-1):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    break

                else:
                    return None # edge case where none of them add to the target

        return list(i, j)


# Test Cases
print(Solution.twoSum(Solution, [1, 3, 5], 6))
