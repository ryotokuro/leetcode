# link: https://leetcode.com/problems/jewels-and-stones/

# PROBLEM
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# EXAMPLE
# Input: J = "aA", S = "aAAbbbb"
# Output: 3


def numJewelsInStones(J: str, S: str) -> int: # parameters str and output is int
    numJewels = 0  # intial condition
    for stone in S:
        if stone in J:
            numJewels += 1
    return numJewels


jewels, stones = input().split(' ')
print(numJewelsInStones(jewels, stones))  # testx
