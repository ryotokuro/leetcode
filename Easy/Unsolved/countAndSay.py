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
#
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

def countAndSay(n):
    # start off with 1
    # 1 :   'one one'         i.e. 11
    # 11:   'two one'         i.e. 21
    # 21:   'one two one one' i.e. 1211
    # 1211: 'one one one two two one' i.e. 111221
    # 111221: 'three one two two one one'
    
    # Base Case


    counter = '1'
    
    while n > 1:
        same = 1
        modified = ''
        
        for i in range(len(counter)):
            curr = counter[i]

            # if it's the last digit
            if i == len(counter)-1:
                modified += str(same) + curr
                
            else:
                after = counter[i+1]
                # compare curr and prev
                if curr == after:
                    same += 1
                    
                # if the next number is different
                else:
                    # create new expression
                    modified += str(same) + curr
                    same = 1
                
        counter = modified
        print(n, ":", counter)
        
        n -= 1

    return counter


#print(countAndSay(1))
countAndSay(3)
print()
countAndSay(4)
print()
countAndSay(5)
print()
# PROBLEM HERE
countAndSay(6)
print()
countAndSay(7)
print()
countAndSay(8)
