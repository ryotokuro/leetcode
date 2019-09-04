# link: https://leetcode.com/problems/sqrtx/

# PROBLEM
# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer,
# the decimal digits are truncated and only the integer part of the result is returned.
#
# EXAMPLE:
# Input: 4
# Output: 2

# EXAMPLE 2
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


def mySqrt(x):
    return int(x**0.5)


print(mySqrt(4))
print(mySqrt(8))
