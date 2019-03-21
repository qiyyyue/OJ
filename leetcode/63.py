# coding: utf8
'''
不同路径
'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0:
            return 0
        elif len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = [[0 for j in range(n)] for i in range(m)]

        if obstacleGrid[0][0] != 1:
            res[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i - 1 >= 0:
                    res[i][j] += res[i - 1][j]
                if j - 1 >= 0:
                    res[i][j] += res[i][j - 1]
        return res[m-1][n-1]