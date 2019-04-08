from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res_nums = []
        for num in range(left, right + 1):
            tag = True
            tmp_num = num
            while tmp_num > 0:
                c = tmp_num % 10
                tmp_num //= 10
                if c == 0 or num % c != 0:
                    tag = False
                    break
            if tag:
                res_nums.append(num)

        return res_nums

