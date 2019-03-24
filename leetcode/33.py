from typing import List


def search(nums: List[int], target: int) -> int:
    if len(nums) == 0:
        return -1
    l = 0
    h = len(nums) - 1
    while h >= l:
        mid = (l + h) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[l]:
            if nums[mid] >= target and nums[l] <= target:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if nums[h] >= target and nums[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
    return -1


nums = [5,1,2,3,4]
target = 1
print(search(nums, target))