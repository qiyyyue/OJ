from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mid_num = nums[len(nums)//2]
        move_steps = 0
        for num in nums:
            move_steps += abs(num - mid_num)
        return move_steps