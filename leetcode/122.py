from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        res = 0
        tmp = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                continue
            res += prices[i - 1] - tmp
            tmp = prices[i]
        res += prices[len(prices) - 1] - tmp
        return res