# PROBLEM
# - Input: s = "PAYPALISHIRING", numRows = 3
# - Output: "PAHNAPLSIIGYIR"
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R

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
#
# Note: I notice that the diagonal is the same length as the number of rows
# -> If I simply add on the number of rows - 2 (the fence posts) then I can get the first row simply
# -> This also consistently retrieves another term for the subsequent rows, but I need to get the extra bits

# 1: 0   6    12   all +6
# 2: 1 5 7 11 13   +4 then +2 pattern
# 3: 2 4 8 10      +2 +4 pattern
# 4:  3   9        all +6

# ---------------------------------------

# numrows = 5
#
# P       H
# A     S I
# Y   I   R
# P L     I G
# A       N

# 1: 0 8        all +8
# 2: 1 7 9      +6  +2
# 3: 2 6 10     +4  +4
# 4: 3 5 11 13  +2  +6
# 5:  4  12     all +8


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