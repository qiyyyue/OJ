

import sys

n = int(sys.stdin.readline().strip())

count = 0


re = 1024 - n
if re >= 64:
    count += re//64
    re = re%64
if re >= 16:
    count += re // 16
    re = re % 16
if re >= 4:
    count += re // 4
    re = re % 4
count += re
print(count)