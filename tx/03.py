


import sys


def dp(target, len, deep, prt_line):

    if len == 1:
        print()
    if target == 0:
        i = 0
        while 2**deep * i + 2**(deep-1) <= n:
            prt_line += str(2**deep * i + 2**(deep-1)) + " "
            i += 1
    else:
        i = 1
        while 2**deep * i <= n:
            prt_line += str(2**deep * i) + " "
            i += 1
        prt_line += str(2**(deep-1)) + " "
    if len%2 == 0:
        return dp(0, len//2, deep + 1, prt_line)
    else:
        return dp(1, len//2, deep + 1, prt_line)

n = int(sys.stdin.readline().strip())
tmp_len = n
target = 0

print(dp(target, n, 1, ""))




