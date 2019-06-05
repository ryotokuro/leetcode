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
    map = dict()
    for i in range(numArray):
        #
        map[i] = numArray

    for key in map:
        if map[key] + map[key+1]  == 0:

        # look for the -x or +y which makes 0 and see if they exist in the list
        # if so then create

    return numArray

numArray = input()