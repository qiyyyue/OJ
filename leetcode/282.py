from typing import List

res_list = []

def addOperators(num: str, target: int) -> List[str]:
    if len(num) == 0:
        return []
    cal_dp(num, target, 0, "", None)
    return res_list

def cal_dp(num: str, target: int, cur_res: int, tmp_res: str, pre_num: int):
    if len(num) == 0 and cur_res == target:
        res_list.append(tmp_res)
        return
    for i in range(1, len(num) + 1):
        cur_number = num[:i]
        if cur_number[0] == '0' and len(cur_number) > 1:
            return
        cur_number = int(cur_number)

        next_numbers = num[i:]
        if len(tmp_res) > 0:
            cal_dp(next_numbers, target, cur_res - pre_num + pre_num *cur_number, tmp_res + "*" + str(cur_number), pre_num *cur_number)
            cal_dp(next_numbers, target, cur_res + cur_number, tmp_res + "+" + str(cur_number), cur_number)
            cal_dp(next_numbers, target, cur_res - cur_number, tmp_res + "-" + str(cur_number), cur_number)
        else:
            cal_dp(next_numbers, target, cur_number, str(cur_number), cur_number)


print(addOperators('105', 5))