# PROBLEM
# Implement atoi which converts a string to an integer.
# The function first:
# - discards as many whitespace characters as necessary until the first non-whitespace character is found.

# Then, starting from this character, takes an optional initial plus or minus sign
# - followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number,
# - which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.


def myAToI(string):
    if string == "" or string == "+" or string == "-":
        return 0

    for i in range(len(string)):
        if string[i] != ' ':  # iterate until no white space
            start = i  # i is now where the first non-white space character is
            break

    if string[i] == '-' or string[i] == '+':  # if a negative or positive symbol is found
        start = i
        i += 1

    if i+1 is len(string):  # if no meaningful number exists in the list
        return 0

    validNumber = str(list(range(10)))  # just compute it once so i don't need to keep doing it

    if string[i] in validNumber:  # if the first character is a +, - or number
        # print(i, "It is a valid number")
        while i < len(string):
            print(i, string[i])
            if string[i] in validNumber and string[i] != ' ':
                i += 1
                continue
            break
        end = i

    else:  # if no valid conversion
        return 0

    print(start, end)
    # if overflow return the MAX integer (2^32 - 1)
    if int(string[start:end]) > ((2 ** 31) - 1):
        return (2 ** 31) - 1

    elif int(string[start:end]) < -((2 ** 31) - 1):
        return -(2 ** 31) - 1

    return int(string[start:end])  # returns the valid number type-casted as an int


# TEST CASES
print(myAToI("   +0 123"))
# print(myAToI("-42"))  # -42
# print(myAToI("+wa"))  # 0
# print(myAToI("4193 with words"))  #4193
# print(myAToI("     +42"))  # 42
# print(myAToI("-91283472332"))  # -2147483648

# USER INPUT
string = str(input())
print(myAToI(string))
