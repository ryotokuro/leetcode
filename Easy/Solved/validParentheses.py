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
        if s == "":
            return True

        brackets = {}
        for i in s:
            if i not in brackets:
                brackets[i] = 1
            else:
                brackets[i] += 1
        print(s, brackets)
        if '()[]{}' in s:
            return brackets['('] == brackets[')'] and brackets['['] == brackets[']'] and brackets['{'] == brackets['}']
        elif '()' in s:
            return brackets['('] == brackets[')']
        elif '[]' in s:
            return brackets['['] == brackets[']']
        elif '{}' in s:
            return brackets['{'] == brackets['}']
        print('None passed')
        return False


# TESTS
print(validParentheses('()'))  # true
print()
print(validParentheses('()[]{}'))  # true
print()
print(validParentheses('(]'))  # false
print()
print(validParentheses('([)]'))  # false
print()
print(validParentheses('{[]}'))  # true
print()
print(validParentheses('([]'))  # false
