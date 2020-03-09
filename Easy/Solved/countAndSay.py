# link: https://leetcode.com/problems/count-and-say/

# PROBLEM
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# EXAMPLES
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

def countAndSay(n):
    # Base Case
    counter = '1'
    
    while n > 1:
        same = 1
        modified = ''

        # Loop through counter's digits
        for i in range(len(counter)):
            curr = counter[i]
            
            # If curr is pointing to the last digit
            if i == len(counter)-1:
                modified += str(same) + curr
                
            else:
                after = counter[i+1]
                # Compare curr with the next digit
                if curr == after:
                    same += 1
                    
                # Otherwise, curr and the next digit are different
                else:
                    # Append the new expression
                    modified += str(same) + curr
                    same = 1  # Reset counter
                    
        counter = modified  # Overwrite counter
        # print(n, ":", counter)  # debugging
        
        n -= 1

    return counter

# 3 -> 21
countAndSay(3)
print()

# 4 -> 1211
countAndSay(4)
print()

# 5 -> 111221
countAndSay(5)
print()

# 6 -> 312211
countAndSay(6)
print()

# 7 -> 13112221
countAndSay(7)

# 8 -> 1113213211
print()
countAndSay(8)
