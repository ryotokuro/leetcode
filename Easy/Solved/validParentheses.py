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

    # 3. Has to have either (), [] or {} in the middle
    middle = s[(length//2)-1:(length//2)+1]  # slice to get middle chunk
    if middle not in '()[]{}':
        print('middle:', middle)
        print('Middle not valid')
        return False

    # # Only works for Nested Loops :(
    # start = 0
    # end = length-1
    # while start < end:  # because its even i need to check if they ever cross paths
    #     if s[start] == '(':
    #         if s[end] != ')':
    #             return False
    #     elif s[start] == '[':
    #         if s[end] != ']':
    #             return False
    #     else:  # assuming only receiving brackets, it has to be curly brace
    #         if s[end] != '}':
    #             return False
    #     start += 1
    #     end -= 1
    # return True

    brackets = {}  # Dictionary in form {Bracket : Position of Complement}
    for pos, val in enumerate(s):
        if val not in brackets:
            if val in '([{':
                if val not in brackets:
                    if '(' in brackets:
                        brackets['('] += 2
                    if '[' in brackets:
                        brackets['['] += 2
                    if '{' in brackets:
                        brackets['{'] += 2
                    brackets[val] = pos + 1
            else:  # it's a closing bracket
                if val == ']' and '[' not in brackets or val == ')' and '(' not in brackets or val == '}' and '{' not in brackets:
                    print('No front bracket')
                    return False  # There was a closing bracket BEFORE its opening bracket partner appeared
                # Ok we've got matching things now good
                if val == ')':
                    if brackets['('] != pos:
                        print('Failed not matching')
                        return False

    print(brackets)
    return True

    # if '()[]{}' in s:
    #     return brackets['('] == brackets[')'] and brackets['['] == brackets[']'] and brackets['{'] == brackets['}']
    # elif '()' in s:
    #     return brackets['('] == brackets[')']
    # elif '[]' in s:
    #     return brackets['['] == brackets[']']
    # elif '{}' in s:
    #     return brackets['{'] == brackets['}']
    # print('None passed')
    # return False


# TESTS
print(validParentheses("[(({})}]"))  # true
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
