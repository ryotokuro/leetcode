# PROBLEM
# - Input: s = "PAYPALISHIRING", numRows = 3
# - Output: "PAHNAPLSIIGYIR"
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R

# 1: 0   4   8    12    +4 +0
# 2: 1 3 5 7 9 11 13    +2 +2
# 3: 2   6   10         +4 (constant for last row)

# --------------------------------------

# And then read line by line: "PAHNAPLSIIGYIR"
#
# EXAMPLE 2
# - Input: s = "PAYPALISHIRING", numRows = 4
# - Output: "PINALSIGYAHRPI"
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# 1: 0   6    12   +6 0
# 2: 1 5 7 11 13   +4 then +2 pattern
# 3: 2 4 8 10      +2 +4 pattern
# 4:  3   9        all +6

# ---------------------------------------

# numRows = 5
#
# P       H
# A     S I
# Y   I   R
# P L     I G
# A       N

# 1: 0 8        +8   0
# 2: 1 7 9      +6  +2
# 3: 2 6 10     +4  +4
# 4: 3 5 11 13  +2  +6
# 5:  4  12     all +8

# NOTE ON RULES
# - On the FIRST and LAST rows you add a constant
#   -> This number is the number of rows + ceil(numRows/2)
# - Inbetween, the rows have an alternating adder patten
# - Going down a row you add 2 to the first number and subtract 2 from the second
# - It should stop when one reaches the other


def convert(s, numRows):  # returns the converted string
    converted = "s[0]"
    diagonal = numRows+1  # k should be the diagonal gap
    # inter should be the bridge gap
    for i in range(0, len(s)):  # go row by row
        # try to append each
        while i+k < len(s):  # ensure we don't go out of bounds
            converted.append(s[i+k])  # PAHN - need to somehow make sure it goes to the second row
    return converted


print(convert("PAYPALISHIRING", 3))  # Test Case 1

print("PAYPALISHIRING", 4)  # Test Case 2

# User Input Methods
string = str(input())
numRows = int(input())

print(convert(string, numRows))