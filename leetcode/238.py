from typing import List


def productExceptSelf( nums: List[int]) -> List[int]:

    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [0]

    res = [1 for i in range(len(nums))]

    res[0] = nums[0]
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i]
    for j in range(len(nums) - 2, -1, -1):
        nums[j] *= nums[j + 1]


    res[len(nums) - 1] = res[len(nums) - 2]

    for i in range(len(nums) - 2, 0, -1):
        res[i] = res[i - 1] * nums[i + 1]

    res[0] = nums[1]

    return res

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))