from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 1

    n = len(nums)
    nums.append(0)

    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] >= n + 1:
            nums[i] = 0

    print(nums)

    for i in range(len(nums)):
        nums[nums[i ] %(n + 1)] += n + 1
    print(nums)
    for i in range(1, len(nums) - 1):
        if nums[i] < n + 1:
            return i
    return n + 1


nums = [7,8,9,10,11]

print(firstMissingPositive(nums))