# coding: utf8

'''
第一个缺失的正数
'''
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        n = len(nums)
        nums.append(0)

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] >= n + 1:
                nums[i] = 0

        for i in range(len(nums)):
            nums[nums[i] % (n + 1)] += n + 1
        for i in range(1, len(nums)):
            if nums[i] < n + 1:
                return i
        return n + 1