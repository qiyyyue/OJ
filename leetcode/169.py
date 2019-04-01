

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        tmp_num = 0
        for num in nums:
            if count == 0:
                tmp_num = num
            if num == tmp_num:
                count += 1
            else:
                count -= 1
        return tmp_num