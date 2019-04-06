from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not len(points):
            return 0

        points = sorted(points, key=lambda x: x[1])

        res = 1

        l_end = points[0][1]

        for point in points[1:]:
            if point[0] > l_end:
                res += 1
                l_end = point[1]
        return res