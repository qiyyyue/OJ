from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def adjustHeap(points: List[List[int]], k: int, start: int):

            mx = start
            l = 2 * mx + 1 if 2 * mx + 1 < k else None
            r = 2 * mx + 2 if 2 * mx + 2 < k else None

            if l and points[mx][0] ** 2 + points[mx][1] ** 2 < points[l][0] ** 2 + points[l][1] ** 2:
                mx = l
            if r and points[mx][0] ** 2 + points[mx][1] ** 2 < points[r][0] ** 2 + points[r][1] ** 2:
                mx = r

            if mx != start:
                points[mx], points[start] = points[start], points[mx]
                adjustHeap(points, k, mx)

        def initHeap(points: List[List[int]], k: int):
            for i in range(k // 2 - 1, -1, -1):
                adjustHeap(points, k, i)

        mx_heap = points[0:K]
        initHeap(mx_heap, K)

        for point in points[K:]:
            if point[0] ** 2 + point[1] ** 2 < mx_heap[0][0] ** 2 + mx_heap[0][1] ** 2:
                mx_heap[0] = point
                adjustHeap(mx_heap, K, 0)

        return mx_heap
