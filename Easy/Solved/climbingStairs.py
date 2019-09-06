# link: https://leetcode.com/problems/climbing-stairs/

# PROBLEM
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.

# EXAMPLE
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# EXAMPLE 2
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Input: 4 (three three, one 1 + 1)
# 1 1 1 1
# 1 1 2
# 2 1 1
# 1 2 1
# 2 2

# Input: 5 (four 4, three 3 + 1)
# 1 1 1 1 1
# 1 1 1 2
# 2 1 1 1
# 1 1 2 1
# 1 2 1 1
# 2 2 1
# 1 2 2
# 2 1 2

def climbStairs(n):


print(climbStairs(2))
print(climbStairs(3))
