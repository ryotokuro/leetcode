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

    # 2. Odd Length (not really an edge case but ensures there are valid pairs)
    if len(s) % 2 != 0:  # if its an odd length
        print('Odd Length')
        return False  # then there aren't PAIRS of brackets definitely

    # 3. Has to have either (), [] or {} in the middle
    middle = s[(len(s)//2)-1:(len(s)//2)+1]
    if middle not in '()[]{}':
        print('middle:', middle)
        print('Middle not valid')
        return False

    # DONT NEED A DICTIOANRY I JUST ITERATE START AND END AND CHECK IF SAME POGCHAMPS

    brackets = {}  # Dictionary in form {Bracket : Position of Complement}
    for pos, val in enumerate(s):
        if val not in brackets:
            if val in '([{':
                brackets[val] = pos + 1
            else:  # it's a closing bracket
                if val == ']' and '[' not in brackets or val == ')' and '(' not in brackets or val == '}' and '{' not in brackets:
                    print('No front bracket')
                    return False  # There was a closing bracket BEFORE its opening bracket partner appeared
                # Ok we've got matching things now good

    print(s, brackets)

    # if '()[]{}' in s:
    #     return brackets['('] == brackets[')'] and brackets['['] == brackets[']'] and brackets['{'] == brackets['}']
    # elif '()' in s:
    #     return brackets['('] == brackets[')']
    # elif '[]' in s:
    #     return brackets['['] == brackets[']']
    # elif '{}' in s:
    #     return brackets['{'] == brackets['}']
    # print('None passed')
    return False


# TESTS
print(validParentheses('()]'))  # true
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
