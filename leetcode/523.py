class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmp_dict = {0: -1}
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            if k != 0:
                sums %= k
            if sums not in tmp_dict:
                tmp_dict[sums] = i
            else:
                tmp = i - tmp_dict[sums]
                if tmp > 1:
                    return True
        return False