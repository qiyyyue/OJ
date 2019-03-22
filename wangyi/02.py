
import sys

mountains = list(map(int, sys.stdin.readline().strip().split(",")))

def longestMountain(A):
    res = 0
    up = 0
    down = 0
    for i in range(1, len(A)):
        if down > 0 and A[i - 1] < A[i] or A[i - 1] == A[i]:
            up = down = 0
        if A[i - 1] < A[i]:
            up += 1
        if A[i - 1] > A[i]:
            down += 1
        if up > 0 and down > 0 and up + down + 1 > res:
            res = up + down + 1
    return res

print(longestMountain(mountains))

