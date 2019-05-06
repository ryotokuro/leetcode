# BACKGROUND
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Where:
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example,
# - Two is written as II in Roman numeral, just two one's added together.
# - Twelve is written as, XII, which is simply X + II.
# - The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.

# There are six instances where subtraction is used:
# - I can be placed before V (5) and X (10) to make 4 and 9.
# - X can be placed before L (50) and C (100) to make 40 and 90.
# - C can be placed before D (500) and M (1000) to make 400 and 900.

def intToRoman(num: int):
    romanNumeral = ""
    while num != 0:
        if num >= 1000:
            romanNumeral += "M"
            num -= 1000
        elif num >= 500:
            romanNumeral += "D"
            num -= 500
        elif num >= 100:
            romanNumeral += "C"
            num -= 100
        elif num >= 50:
            romanNumeral += "L"
            num -= 50
        elif num >= 10:
            romanNumeral += "X"
            num -= 10
        elif num >= 9:
            romanNumeral += "IX"
            num -= 9
        elif num >= 5:
            romanNumeral += "V"
            num -= 5
        elif num >= 4:
            romanNumeral += "IV"
            num -= 4
        elif num >= 1:
            romanNumeral += "I"
            num -= 1
    return romanNumeral


# TEST CASES
print(intToRoman(3))  # III
print(intToRoman(4))  # IV
print(intToRoman(9))  # IX
print(intToRoman(58))  # LVIII
print(intToRoman(1994))  # MCMXCIV

num = int(input())
intToRoman(num)
