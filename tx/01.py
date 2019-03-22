import sys



line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
values = list(map(int, line.split()))
n = values[0]
a = values[1]

X = list(map(int, sys.stdin.readline().strip().split()))


l1 = 0
l2 = 0


if a < X[0]:
    l1 = X[n - 2] - a
elif a > X[n - 1]:
    l1 = a - X[1]
elif a == X[0]:
    l1 = X[n - 2] - X[0]
elif a == X[n - 1]:
    l1 = X[n - 1] - X[1]
else:
    tmp1 = a - X[0] + X[n - 2] - X[0]
    tmp2 = X[n - 2] - a + X[n - 2] - X[0]
    tmp3 = X[n - 1] - a + X[n - 1] - X[1]
    tmp4 = a - X[1] + X[n - 1] - X[1]
    l1 = min(tmp1, min(tmp2, min(tmp3, tmp4)))



print(l1 + l2)