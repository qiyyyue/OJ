from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num, alpha = [], []
        for s in logs:
            if s[-1].isdigit():
                num.append(s)
            else:
                alpha.append(s)

        alpha = sorted(alpha, key=lambda s: s[s.index(' '):])
        return alpha + num