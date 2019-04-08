from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        t_dict = {}
        for i in range(len(numbers)):
            if target-numbers[i] in t_dict:
                return t_dict[target-numbers[i]] + 1, i + 1
            else:
                t_dict[numbers[i]] = i
        return []