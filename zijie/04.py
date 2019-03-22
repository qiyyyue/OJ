
import sys

n_m = list(map(int, sys.stdin.readline().strip().split()))
n = n_m[0]
m = n_m[1]

lens = list(map(int, sys.stdin.readline().strip().split()))

lens = sorted(lens, reverse=True)

if m <= n:
    lens = lens[0:m]

print(lens[m - 1])