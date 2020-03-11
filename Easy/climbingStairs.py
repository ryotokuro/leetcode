# https://leetcode.com/problems/climbing-stairs/

# You are climbing a stair case.
# It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


# RECURSIVE
def climbStairs(n):
    """Too slow, time complexity is O(2^n)"""
    if n == 0:
        return 1
    elif n < 0:
        return 0

    # It's greater than 0, so you can keep taking off more
    return climbStairs(n-1) + climbStairs(n-2)


# ITERATIVE
def climbStairs(n):
    """Generates the sequence dynamically, O(n)"""
    if n < 2:
        return n

    left = 0
    right = 1
    for _ in range(n, 0, -1):
        node = left + right
        left = right
        right = node
    return right
    
print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(38))

