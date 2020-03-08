# Given a 32-bit signed integer, reverse digits of an integer.

#def reverse(self, num: int) -> int:
def reverse(n):
    num = str(n) # Convert to string for simple manipulation

    # CASES
    # Empty input
    if not num:
        return 0
    
    # One digit number
    if len(num) == 1:
        return int(num)

    MAX = pow(2, 31) - 1

    # Negative number
    if num[0] == '-':
        # Check for underflow
        if abs(int(num[:0:-1])) > MAX:
            return 0
        num = '-' + num[1:len(num)][::-1]  # Return reversed number with negative sign

    # Reversed number is too big
    elif abs(int(num[::-1])) > MAX:
        return 0  # number overflowed

    # Safe: num is a normal number
    else:
        num = num[::-1]  # simply reverses the number

    # RETURN
    # For floating point numbers
    if '.' in num:
        return float(num)

    # Return as an integer
    return int(num)


# Normal
print(reverse(123))  # 321
# Negative
print(reverse(-123))  # -321
# 0 at the end
print(reverse(120))  # 21
# 0 as input
print(reverse(0))
# Overflow
print(reverse(1534236469))
# Negative Overflow
print(reverse(-2147483648))
