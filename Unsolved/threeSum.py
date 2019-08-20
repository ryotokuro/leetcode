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
    trial = solution = list()  # an array of arrays
    map = dict()

    for i in range(numArray-1):
        for j in range(i+1, numArray):
            trial.append(numArray[i] + numArray[j])
            # need to get the index too!
            print(numArray[i]+numArray[j])
            map[i, j] = numArray[i]+numArray[j]

    for i in range(trial):
        print(map)
    return numArray


numArray = input()