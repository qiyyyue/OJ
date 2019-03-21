'''

'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_up_len = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    max_up_len[i] = max(max_up_len[i], max_up_len[j] + 1)
        return max(max_up_len)