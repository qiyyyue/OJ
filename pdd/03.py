from typing import List


def solution(nums: List[int], d: int) -> float:
    nums = sorted(nums)
    print(nums)
    count = 0
    last_count = 0
    i = 0
    j = 1
    while i < len(nums):
        j = max(j, i + 1)
        while j < len(nums) and nums[j] - nums[i] <= d:
            last_count += 1
            j += 1
        count += last_count
        last_count = max(last_count - 1, 0)
        i += 1
    return format((float(count)/len(nums)/(len(nums)-1)*2), '.6f')

nums = [31, 18, 19, 1, 25]
d = 10
print(solution(nums, d))