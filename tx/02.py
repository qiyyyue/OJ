


import sys




n = int(sys.stdin.readline().strip())
s = []
for i in range(n):
    s.append(int(sys.stdin.readline().strip()))
v = [[0, 0, 0] for x in range(n)]
v[0][0] = 0
v[0][1] = 0
v[0][2] = s[0]
v[1][0] = 0
v[1][1] = s[0]
v[1][2] = s[1]

for i in range(1, n):
    v[i][2] = min(v[i-1][2] + s[i], v[i-1][1] + s[i], v[i-1][0] + s[i])
    v[i][1] = v[i-1][2]
    v[i][0] = v[i-1][1]

print(min(v[n-1][0], v[n-1][1]))