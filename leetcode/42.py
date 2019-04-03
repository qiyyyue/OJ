from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0] * len(height)
        r = [0] * len(height)

        for i in range(1, len(height)):
            l[i] = max(l[i - 1], height[i - 1])
        for j in range(len(height) - 2, -1, -1):
            r[j] = max(r[j + 1], height[j + 1])

        res = 0
        for k in range(1, len(height) - 1):
            res += max(min(l[k], r[k]) - height[k], 0)

        return res