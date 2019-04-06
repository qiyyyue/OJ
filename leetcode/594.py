from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        # print(count_dict)
        max_count = 0
        for num in count_dict:
            tmp_count = 0
            if num + 1 in count_dict:
                tmp_count += count_dict[num + 1]
            if num - 1 in count_dict:
                tmp_count = max(count_dict[num - 1], tmp_count)
            tmp_count = count_dict[num] + tmp_count if tmp_count > 0 else 0
            if tmp_count > max_count:
                max_count = tmp_count

        return max_count