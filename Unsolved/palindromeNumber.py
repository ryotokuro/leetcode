def isPalindrome(num: int):
    # METHOD 1 (using string conversion)
    # if str(num) == str(num)[::-1]:
       # return True
    # return False  # returns boolean true/false

    # METHOD 2 (no string)
    return (num - (num % 10)) % 100


# TEST CASES
print(isPalindrome(121))   # true
print(isPalindrome(-121))  # false
print(isPalindrome(10))    # false

# Could you solve it without converting the integer to a string?
num = int(input())
print(isPalindrome(num))
