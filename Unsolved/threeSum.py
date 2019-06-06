# PROBLEM
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# EXAMPLE
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# def threeSum(numArray: List[int]) -> List[List[int]]:
def threeSum(numArray: list[int]):
    solution = list()  # an array of arrays
    # map numbers in the set to a hashmap
    for i in range(numArray-1):
        for j in range(i+1, numArray):
            numArray[i] + numArray[j]

    return numArray

numArray = input()