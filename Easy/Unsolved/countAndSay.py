# link: https://leetcode.com/problems/count-and-say/

# PROBLEM
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
#
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

def countAndSay(n):
    # start off with 1
    # 1 :   'one one'         i.e. 11
    # 11:   'two one'         i.e. 21
    # 21:   'one two one one' i.e. 1211
    # 1211: 'one one one two two one' i.e. 111221
    # 111221: 'three one two two one one'
    if n == 1:
        return '1'

    # start off with 1
    num = list('11')
    i = 1
    for i in range(len(n)):
        for i in range()

    print(num)
    return '5'

countAndSay(1)
countAndSay(4)