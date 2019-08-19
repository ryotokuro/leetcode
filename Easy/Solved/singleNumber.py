def singleNumber(nums):
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]  # XOR returns 0 if the numbers are the same and 1 if they're different
    return nums[0]
    # if len(nums) == 1:
    #     return nums[0]
    #
    # nums.sort()  # so in the same order
    # print(nums)
    #
    # # then traverse by 2
    # i = 0
    # j = 1
    # while j < len(nums):
    #     print(nums[i], nums[j])
    #     if nums[i] != nums[j]:
    #         break
    #     i += 2
    #     j += 2
    #
    # if i == 0 or i == len(nums)-1 or nums[i] != nums[i - 1]:
    #     return nums[i]
    # else:
    #     return nums[j]


print(singleNumber([2, 2, 1]))  # 1 1 2
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([17, 12, 5, -6, 12, 4, 17, -5, 2, -3, 2, 4, 5, 16, -3, -4, 15, 15, -4, -5, -6]))
