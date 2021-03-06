# link: https://leetcode.com/problems/fizz-buzz/submissions/

# PROBLEM
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.

# EXAMPLE
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


def fizzBuzz(n: int):
    string = []

    i = 1
    # for i in range(i, len(n)):
    # for loop is SLOWER than while loop if we use RANGE
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            string.append("FizzBuzz")
        elif i % 3 == 0:
            string.append("Fizz")
        elif i % 5 == 0:
            string.append("Buzz")
        else:
            string.append(str(i))
        i += 1
    return string


print(fizzBuzz(15))
