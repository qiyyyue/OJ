import sys


class Solution():
    def __init__(self):
        self.c_dict = {'(': ')', '[': ']', '{': '}'}
    def cal_str(self, org_str: str) -> str:
        res_str = ''
        i = 0
        while i < len(org_str):
            if org_str[i].isdigit():
                tmp_c = org_str[i+1]
                tmp_c_pair = self.c_dict[tmp_c]
                tmp_c_count = 0
                #print(i, tmp_c, tmp_c_pair)
                for j in range(i+1, len(org_str)):
                    if org_str[j] == tmp_c:
                        tmp_c_count += 1
                    if org_str[j] == tmp_c_pair:
                        tmp_c_count -= 1
                        if tmp_c_count == 0:
                            #print(i, j)
                            tmp_str = self.cal_str(org_str[i+2:j])
                            for k in range(int(org_str[i])):
                                res_str = tmp_str + res_str
                            i = j
            else:
                res_str = org_str[i] + res_str
            i += 1

        return res_str

in_str = sys.stdin.readline().strip()

s = Solution()
print(s.cal_str(in_str))



