# link: https://leetcode.com/problems/to-lower-case/

# PROBLEM
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.


def toLowerCase(string: str) -> str:
    uppercases = set()  # store uppercases we find in a set since strings are immutable
    for index, letter in enumerate(string):
        if letter.isupper():  # it is not lowercase, we need to change it...
            print(chr(ord(letter) + 32))
    # return string.lower()

    # then go into another loop
    # in this we SPLIT by the upper characters and then "".join

    return string


string = input()
print(toLowerCase(string))
