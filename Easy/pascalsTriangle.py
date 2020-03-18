# https://leetcode.com/problems/pascals-triangle/

def generate(numRows):
        if numRows == 0:
            return []

        elif numRows == 1:
            return [[1]]
        
        start = [[1], [1,1]]
        
        while len(start) != numRows:
            i = 0
            j = 1
            new_row = [1]
            last_row = start[len(start)-1]
            while j < len(last_row):
                new_row.append(last_row[i] + last_row[j])
                i = j
                j += 1
                
            new_row.append(1)  
            start.append(new_row)
        
        return start

generate(5)
generate(0)
