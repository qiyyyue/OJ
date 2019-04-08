from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        max_len = [1] * len(A[0])
        for i in range(len(A[0])):
            for j in range(i):
                for k in range(len(A) + 1):
                    if k == len(A):
                        max_len[i] = max(max_len[i], max_len[j] + 1)
                        break
                    if A[k][j] > A[k][i]:
                        break
        return len(A[0]) - max(max_len)