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

        targetReached = False

        # using HASH TABLE - trading space for time
        nums['one'] = nums[0]
        nums['two'] = nums[1]
        nums['three'] = nums[2]

        if nums['one'] + nums[1]
        
        for i in range(len(nums)-1):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    targetReached = True
                    break

                j += 1  # need to increment or stuck in loop

            if targetReached:
                break

        if not targetReached:
            return None  # edge case where none of them add to the target

        return [i, j]


# Test Cases
print(Solution.twoSum(Solution, [2, 7, 11, 15], 9))
print(Solution.twoSum(Solution, [0, 0, 0], 1))
print(Solution.twoSum(Solution, [3, 2, 4], 6))
