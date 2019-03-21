class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        intes = []

        for i in range(26):
            if S.count(chr(ord("a") + i)):
                intes.append([S.find(chr(ord("a") + i)), S.rfind(chr(ord("a") + i))])

        intes = sorted(intes, key=lambda x: x[0])

        l = intes[0][0]
        r = intes[0][1]

        res = []

        for inte in intes:
            if inte[0] <= r:
                r = max(r, inte[1])
            else:
                res.append([l, r])
                l = inte[0]
                r = inte[1]
        res.append([l, r])

        return [x[1] - x[0] + 1 for x in res]