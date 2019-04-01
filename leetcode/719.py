from typing import List


def smallestDistancePair(nums: List[int], k: int) -> int:
    if len(nums) == 0:
        return None

    nums.sort()
    l = 0
    r = nums[len(nums) - 1] - nums[0]

    while l < r:
        m = l + (r - l) // 2
        j = cnt = 0
        for i in range(1, len(nums)):
            while nums[i] - nums[j] > m:
                j += 1
            cnt += i - j
        if cnt < k:
            l = m + 1
        else:
            r = m
    return l

print(smallestDistancePair([1, 6, 1], 3))