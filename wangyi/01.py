
import sys

n, m = list(map(int, sys.stdin.readline().strip().split(", ")))

def solution(n, m):
    if m > n:
        return 0
    target = 1
    for i in range(2, m + 1):
        target = next(target, n)
    return target


def next(start, n):
    if start == n:
        return start // 10 + 1
    if start > 10 and start % 10 == 9:
        return after9(start, n)

    tmp = start * 10
    if tmp <= n:
        return tmp
    return start + 1

def after9(m, n):
    tmp = m * 10
    if tmp <= n:
        return tmp

    tmp = m + 1
    tmp //= 10
    while tmp % 10 == 0:
        tmp //= 10

    if tmp < 10:
        return tmp
    return (m + 1) // 10

print(solution(n, m))



