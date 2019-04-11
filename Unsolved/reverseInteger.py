# Given a 32-bit signed integer, reverse digits of an integer.
#class Solution:
    #def reverse(self, num: int) -> int:
def reverse(num):
    num = str(num)

    # num is a negative number
    if num[0] == "-":
        num = "-" + num[1:len(num)][::-1]  # returns reversed number holding the negative sign

    # if the last digit is 0 (redundant)
    elif num[-1] == "0":
        num = num[:len(num)-1][::-1]  # returns the reversed number excluding the last digit

    # if the converted string and casted back is different
    elif int(num[::-1]) >= pow(2, 31):
        num = 0  # num overflows

    else:  # num is a normal number
        num = num[::-1]  # simply reverses the number

    return int(num)  # returns result from conditions above

print(reverse( ))
print(reverse(123))  # 321
print(reverse(-123))  # -321
print(reverse(120))  # 21
print(reverse(7463847412))  # overflows
