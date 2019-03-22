
import sys
from queue import Queue

prt = ""

n = int(sys.stdin.readline().strip())

a = Queue(n + 1)

for i in range(n):
    a.put(i + 1)


while not a.empty():
    aa = a.get()
    if not a. empty():
        ab = a.get()
        a.put(ab)
    prt += str(aa) + " "


print(prt)