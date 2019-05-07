# BACKGROUND
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# EXAMPLE
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II.
# The number twenty seven is written as XXVII, which is XX + V + II.

# INFO
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# - I can be placed before V (5) and X (10) to make 4 and 9.
# - X can be placed before L (50) and C (100) to make 40 and 90.
# - C can be placed before D (500) and M (1000) to make 400 and 900.

# PROBLEM
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.


def romanToInteger(roman):
    i = total = 0
    while i < len(roman):
        #print("first", i, roman[i])
        if roman[i] == "M":
            total += 1000

        elif roman[i] == "D":
            total += 500

        elif roman[i] == "C":
            if roman[i+1] == "M":
                total += 900
                i += 1
            elif roman[i+1] == "D":
                total += 500
                i += 1
            else:
                total += 100

        elif roman[i] == "L":
            total += 50

        elif roman[i] == "X":
            if i+1 < len(roman):
                if roman[i+1] == "C":
                    total += 90
                    i += 1

                elif roman[i+1] == "L":
                    total += 40
                    i += 1
            else:
                total += 10

        elif roman[i] == "V":
            total += 5

        elif roman[i] == "I":
            if i+1 < len(roman):
                if roman[i+1] == "X":
                    total += 9
                    i += 1
                elif roman[i+1] == "V":
                    total += 4
                    i += 1

            else:
                total += 1
        i += 1
    return total


# TESTS
print(romanToInteger("III"))      # 3
print(romanToInteger("IV"))       # 4
print(romanToInteger("IX"))       # 9
print(romanToInteger("LVIII"))    # 58
print(romanToInteger("MCMXCIV"))  # 1994

# INPUT READER
roman = str(input())
