import sys
from typing import List


class Solution():

    def pro_single_str(self, org_str: str) ->List[str]:
        res_strs = []
        while len(org_str) > 8:
            res_strs.append(org_str[:8])
            org_str = org_str[8:]
        if org_str:
            res_strs.append(org_str + '0'*(8-len(org_str)))
        return res_strs


    def pro_strs(self) -> List[str]:
        inputs = list(map(str, sys.stdin.readline().strip().split()))
        n = int(inputs[0])
        res_strs = []
        org_strs = inputs[1:]
        for org_str in org_strs:
            res_strs += self.pro_single_str(org_str)
        res_strs = sorted(res_strs, key=lambda x:x[0])
        return res_strs


s = Solution()
print(s.pro_strs())