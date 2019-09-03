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
    # more practical solution O(n)
    # the point here is trying to avoid using in-built functions
    num = 0  # to store the converted number
    for i in range(len(digits)):
        num += pow(10, len(digits)-1-i)*digits[i]  # get the decimal value of the digit and add that to num
    return list(str(num + 1))

    # # alternate solution using a for loop O(n)
    # - in feasible because you have to push new heads to the list at the end too
    # - much easier without having to do so
    # if digits[-1] == 9:
    #     digits[-1] = 0
    #     for i in range(len(digits)-2, -1, -1):
    #         if i == 0:
    #             if digits[i]+1 == 10:
    #                 digits[i] = 0
    #                 digits.insert(0, 1)
    #                 break
    #             else:
    #                 digits[i] += 1
    #         elif digits[i]+1 == 10:
    #             digits[i] = 0
    #         else:
    #             digits[i] += 1
    #             break
    #
    # return list(map(str, digits))

    # # 36ms, 13.8MB
    # digits = list(map(str, digits))  # convert to string instances
    # converted_num = int(''.join(digits))  # join the array and convert it into an integer
    #
    # return list(str(converted_num+1))  # add 1 to that number, convert it to a str and then into a list


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([1, 9, 9]))
