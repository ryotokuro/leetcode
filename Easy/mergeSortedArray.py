# https://leetcode.com/problems/merge-sorted-array/
"""
    [-1, 4, 6, 7, 0, 0, 0, 0]
    [-3, 2, 3, 8]
    m = 4, n = 4
    m + n - 1 = 7
    nums1[m+n-1] > nums2[n-1] (last ele of nums2)
    nums[m+n-1] = nums2[m-1]
    [-3, -1, 6, 7, 0, 0, 0, 0]
"""

def merge(nums1, m, nums2, n):
    # walk through the longer one (nums1) and see if you can insert
    nums1 = nums1[:n]
    
    i = 0
    j = 0
    while i < len(nums1):
        try:
            # compare nums1 item and nums2
            if nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                j += 1
        except:
            break
        i += 1

    nums1 += nums2[j:]
    return nums1

#print(merge([1,2,3,0,0,0], [2,5,6], m=3, n=3))
#print(merge([-1, 3, 4, 6, 0, 0, 0, 0], [-3, 2, 5, 8], m=4, n=4))
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
