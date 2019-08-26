# link: https://leetcode.com/problems/valid-parentheses/

# PROBLEM
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
#
# Note: an empty string is also considered valid.

# EXAMPLE
# Input: "()"
# Output: true

# EXAMPLE 2
# Input: "()[]{}"
# Output: true

# EXAMPLE 3
# Input: "(]"
# Output: false

# EXAMPLE 4
# Input: "([)]"
# Output: false

# EXAMPLE 5
# Input: "{[]}"
# Output: true


def validParentheses(s: str):
    # EDGE CASES
    # 1. Empty String
    if s == "":
        return True

    length = len(s)
    # 2. Odd Length (not really an edge case but ensures there are valid pairs)
    if length % 2 != 0:  # if its an odd length
        print('Odd Length')
        return False  # then there aren't PAIRS of brackets definitely

    # 40ms using 13.8MB Space
    # Using a STACK: uses append() and pop(), where pop() can return the top
    stack = []
    for i in s:
        print('STACK:', stack)
        if not stack:  # empty lists (returns False if empty)
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            else:
                return False  # premature close before an open exists
        else:  # the stack has stuff in it already
            if i == ')' or i == ']' or i == '}':
                if i != stack.pop():
                    return False
            else:
                if i == '(':
                    stack.append(')')
                elif i == '[':
                    stack.append(']')
                elif i == '{':
                    stack.append('}')
    if not stack:
        return True
    else:
        return False


# TESTS
print(validParentheses("(("))  # false
# print(validParentheses("[(({}))]"))  # true
# print()
# print(validParentheses('()[]{}'))  # true
# print()
# print(validParentheses('(]'))  # false
# print()
# print(validParentheses('([)]'))  # false
# print()
# print(validParentheses('{[]}'))  # true
# print()
# print(validParentheses('([]'))  # false
