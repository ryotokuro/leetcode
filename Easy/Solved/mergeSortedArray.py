# link: https://leetcode.com/problems/merge-sorted-array/

# PROBLEM
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space
# -> (size that is greater or equal to m + n) to hold additional elements from nums2.

# EXAMPLE
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]


def merge(nums1, m, nums2, n):
    if not nums1:
        return nums2
    elif not nums2:
        return nums1

    print(nums1,nums2)

    nums3 = []
    i = 0
    j = 0
    while nums2 or nums1[i] != 0:
        if nums1[i] > nums2[j]:
            nums3.append(nums2.pop(0))
            j += 1
        else:
            nums3.append(nums1.pop(0))
            i += 1
    if nums2:
        nums3 += nums2
        print(nums1, nums2, nums3)
    return nums3


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([5, 6, 7, 0, 0, 0], 3, [1, 2, 3], 3))
