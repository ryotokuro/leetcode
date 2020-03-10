# link: https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums,
# find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# EXAMPLE
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach.

# TRIVIAL O(n^2)
def maxSubArray(nums):
    """Calculate largest sum for each item in nums and find max"""
    return 0

# KADANE'S ALGORITHM
def maxSubArray(nums):
    """For Kadane's Algorithm, dynamically find the max sum by deciding
    whether it's better to add the current element, or nothing (zero)
    to the current sum.
    - i.e. positive values (> 0) are encouraged and negatives are discarded"""    
    # a) Similar to Wiki
    curr_sum = 0
    max_sum = 0
    
    for i in nums:
        # Is it better to add 0 or add the current number (i)?
        # - Choosing 0 resets the curr_sum since the subarray sum was negative
        curr_sum = max(0, i+curr_sum)
        max_sum = max(curr_sum, max_sum)  # store largest sum as we're traversing
    return max_sum

# OWN SOLUTION (with help)
def myMaxSubArray(nums):
    """Own interpretation (without using max and modifying existing array)"""
    # Edge case: empty list
    if not nums:
        return 0

    # Edge case: only 1 item in list
    elif len(nums) == 1:        
        return nums[0]
    
    for i in range(1, len(nums)):
        # If the previous number is positive, then it has potential to increase the current sub-sum!
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
            
    return max(nums)  # nums now contains all the greatest subarray sums
    

    # now the var most has the largest value in the list
    # might have to use kadane's algorithm from this point?
    # https://www.youtube.com/watch?v=86CQq3pKSUw

    # optimisation problem (need to check through O(n^2)...

def divideAndConquer(nums):
    for index, value in enumerate(nums):
        if value >= 0:
            break
    #print(nums[index:len(nums)+1])
    return sum(nums[index:len(nums)+1])


print("Kadane:", maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print("Me:", myMaxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print("D&C:", divideAndConquer([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print("Kadane:", maxSubArray([3, 6, 21, 1, 43, 0, 21]))
print("Me:", myMaxSubArray([3, 6, 21, 1, 43, 0, 21]))
print("D&C:", divideAndConquer([3, 6, 21, 1, 43, 0, 21]))
