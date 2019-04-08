from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        l, r = 0, 1
        while l < r:
            m = (l + r)/2
            i = len(A) - 1
            count = 0
            cur = [A[0]/A[-1], A[0], A[-1]]
            for j in range(len(A) - 1, -1, -1):
                while i > -1 and A[i]/A[j] > m:
                    i -= 1
                if i < 0:
                    break
                count += i + 1
                if A[i]/A[j] > cur[0]:
                    cur = [A[i]/A[j], A[i], A[j]]
            if count == K:
                return cur[1:]
            if count < K:
                l = m
            else:
                r = m