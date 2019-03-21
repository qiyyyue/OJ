
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_set = set(s)
        if len(c_set) == 1:
            return len(s)
        elif len(c_set) == 0:
            return 0

        count1 = 0
        count2 = 0
        for c in c_set:
            if s.count(c ) %2 == 0:
                count1 += s.count(c)
            elif s.count(c) > 1:
                count1 += s.count(c) - 1
                count2 = 1
            else:
                count2 = 1
        return count1 + count2