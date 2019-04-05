from typing import List


'''
调整堆
points: 数组
k：数组长度
start：调整的点
'''
def adjustHeap(points: List[int], k: int, start: int):

    mx = start
    l = 2 * mx + 1 if 2 * mx + 1 < k else None
    r = 2 * mx + 2 if 2 * mx + 2 < k else None
    if l and points[mx] < points[l]:
        mx = l
    if r and points[mx] < points[r]:
        mx = r

    if mx != start:
        points[mx], points[start] = points[start], points[mx]
        adjustHeap(points, k, mx)

'''
建堆
points：数组
k：数组长度
'''
def initHeap(points: List[int], k: int):
    for i in range(k // 2 - 1, -1, -1):
        adjustHeap(points, k, i)

'''
'''
def solution(num, projCmptDec, restDec, errorScore):
    #建堆
    initHeap(errorScore, num)
    count = 0
    #堆顶不为零
    while errorScore[0] > 0:
        count += 1
        #堆顶-p
        errorScore[0] = max(0, errorScore[0] - projCmptDec)
        for i in range(1, num):
            #其他元素-q
            errorScore[i] = max(0, errorScore[i] - restDec)
        #调整堆顶
        adjustHeap(errorScore, num, 0)

    return count

num = 4
projCmptDec = 3
restDec = 1
errorScore = [9, 8, 2, 5]

print(solution(num, projCmptDec, restDec, errorScore))