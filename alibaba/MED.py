
import sys


def cal_min_edit_dis(str1: str, str2: str):

    len1 = len(str1)
    len2 = len(str2)

    dis = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

    for i in range(len1 + 1):
        dis[i][0] = i
    for i in range(len2 + 1):
        dis[0][i] = i

    tmp = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                tmp = 0
            else:
                tmp = 1
            dis[i][j] = min(dis[i - 1][j - 1] + tmp, dis[i][j - 1] + 1, dis[i - 1][j] + 1)

    return dis[len1][len2]


str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

print(cal_min_edit_dis(str1, str2))