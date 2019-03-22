import sys

n = int(sys.stdin.readline().strip())

def ss():
    s = sys.stdin.readline().strip()

    count = [0 for x in range(len(s))]

    tmp_c = s[0]
    count[0] = 1

    print(solution(s, count, 1, tmp_c))

def solution(s, count, index_i, tmp_c):
    if index_i >= len(s):
        return s
    if index_i == len(s) - 1:
        if s[index_i] == tmp_c:
            count[index_i] = count[index_i - 1] + 1
            if count[index_i] == 3:
                return s[:index_i]
            elif count[index_i] == 2 and index_i - 2 >= 0 and count[index_i-2] == 2:
                return s[:index_i]
        return s
    for i in range(index_i, len(s)):
        if s[i] == tmp_c:
            count[i] = count[i - 1] + 1
            if count[i] == 3:
                return solution(s[:i] + s[i+1:], count[:i] + count[i+1:], i, tmp_c)
            elif count[i] == 2 and i - 2 >= 0 and count[i-2] == 2:
                return solution(s[:i] + s[i + 1:], count[:i] + count[i+1:], i, tmp_c)
        else:
            count[i] = 1
            tmp_c = s[i]



for i in range(n):
    ss()

# import sys
#
# n = int(sys.stdin.readline().strip())
#
# def solution():
#     s = sys.stdin.readline().strip()
#
#     count_i = 0
#     count_j = 0
#
#     count = [0 for x in range(len(s))]
#
#     flag = [True for x in range(len(s))]
#
#     tmp_c = s[0]
#     count[0] = 1
#     for i in range(1, len(s)):
#         if s[i] == tmp_c:
#             count[i] = count[i - 1] + 1
#         else:
#             count[i] = 1
#             tmp_c = s[i]
#
#     for i in range(len(s)):
#         if count[i] == 3:
#             flag[i] = False
#             j = i + 1
#             count[i] = 0
#             while j < len(s) and s[j] == s[i]:
#                 count[j] -= 1
#                 j += 1
#         elif count[i] == 2 and i - 2 >= 0 and count[i-2] == 2:
#             flag[i+2] = False
#             j = i + 1
#             while j < len(s) and s[j] == s[i]:
#                 count[j] -= 1
#                 j += 1
#     re_s = ""
#     for i in range(len(s)):
#         if flag[i]:
#             re_s += s[i]
#     print(re_s)
#
#
#
# for i in range(n):
#     solution()