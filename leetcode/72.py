# coding: utf8

'''
编辑距离
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        dis = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

        for i in range(len1 + 1):
            dis[i][0] = i
        for i in range(len2 + 1):
            dis[0][i] = i

        tmp = 0

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    tmp = 0
                else:
                    tmp = 1
                dis[i][j] = min(dis[i - 1][j - 1] + tmp, dis[i][j - 1] + 1, dis[i - 1][j] + 1)

        return dis[len1][len2]
