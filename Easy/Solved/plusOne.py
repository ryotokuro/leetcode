# link: https://leetcode.com/problems/plus-one/

# PROBLEM
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# EXAMPLE
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# EXAMPLE 2
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


def plusOne(digits):
    # 36ms, 13.8MB
    digits = list(map(str, digits))  # convert to string instances
    converted_num = int(''.join(digits))  # join the array and convert it into an integer

    return list(str(converted_num+1))  # add 1 to that number, convert it to a str and then into a list


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
