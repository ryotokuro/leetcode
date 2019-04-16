# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.


def maxArea(input):
    # area is dependent on width * height
    # therefore we take the greatest i (mapped) and the tallest height and compute
    # as such we need to maximise w*h (i.e take the greatest i and h)

    # first need to prioritise height
    # then look for the gaps between the heights
    # because sorting is average O(nlogn) i want to try and minimise it and go through the loop once instead

    # note: height is the indexed value, while the INDEX gap is the width
    # should start i at 1 to find the gap easily (largest index - lower index)

    # n must be at least 2, if it is 2 (edge) then just return that
    if len(input()) == 2:
        if input[0] > input[1]:
            return input[1]  # return the second tallest
        else:
            return input[0]

    heightToIndex = dict()
    for i in range(len(input)):
        heightToIndex[input[i]] = i
    
    width = input[] - input[]
    return height*width


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
