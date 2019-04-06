from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for num in nums:
            if num % (len(nums) + 1) == len(nums):
                continue
            else:
                nums[num % (len(nums) + 1)] += len(nums) + 1

        for i in range(len(nums)):
            if nums[i] < len(nums) + 1:
                return i
        return len(nums)