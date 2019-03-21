class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies_set = set(candies)

        return len(candies) // 2 if len(candies_set) > len(candies) // 2 else len(candies_set)