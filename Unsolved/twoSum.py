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

        # using HASH TABLE - trading space for time
        # first add element value and index to the table
        hashMap = dict()
        for i in range(len(nums)):
            hashMap[str(i)] = nums[i]

        print(hashMap)
        # then check if elements complement exists in table (target - nums[i])
        # but CANNOT be nums[i] itself! (index must be different)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap.values() and int(list(hashMap.keys())[list(hashMap.values()).index(complement)]) != nums[i]:
                return [i, int(list(hashMap.keys())[list(hashMap.values()).index(complement)])]

        return None
        #return [i, j]


# Test Cases
print(Solution.twoSum(Solution, [2, 7, 11, 15], 9))
print(Solution.twoSum(Solution, [0, 0, 0], 1))
print(Solution.twoSum(Solution, [3, 2, 4], 6))
print(Solution.twoSum(Solution, [3, 3], 6))
