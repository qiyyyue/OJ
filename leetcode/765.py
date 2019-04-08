from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:

        count_swap = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            if p1 % 2 == 0:
                p2 = p1 + 1
            else:
                p2 = p1 - 1
            if row[i + 1] != p2:
                p3_index = row.index(p2)
                row[i + 1], row[p3_index] = row[p3_index], row[i + 1]
                count_swap += 1
        return count_swap