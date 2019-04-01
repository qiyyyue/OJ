from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def cal_dress(str):
            l, d = str.split("@")
            res = ""
            for c in l:
                if c == '+':
                    break
                elif c == '.':
                    continue
                res += c
            return res + '@' + d

        res_list = []
        for dress in emails:
            dress = cal_dress(dress)
            if dress not in res_list:
                res_list.append(cal_dress(dress))
        return len(res_list)