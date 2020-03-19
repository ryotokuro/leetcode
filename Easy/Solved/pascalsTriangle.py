# https://leetcode.com/problems/pascals-triangle/

def generate(numRows):
        # Edge Case: n = 0
        if numRows == 0:
            return []

        # Edge Case: n = 1
        elif numRows == 1:
            return [[1]]

        # So we can say n > 2 at this point
        triangle = [[1], [1,1]]  # so our triangle beings with 2 rows
        
        while len(triangle) != numRows:
            last_row = triangle[-1]  # grab the last row in the triangle
            new_row = [1]  # new row begins with 1
            i = 0
            while i + 1 < len(last_row):
                # calculate and append the element
                new_row.append(last_row[i] + last_row[i+1])
                i += 1
                
            new_row.append(1)  # don't forget to add 1
            triangle.append(new_row)
        return triangle


# TESTS
assert generate(0) == []
assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], "Expected [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"
