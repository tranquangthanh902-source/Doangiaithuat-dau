class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [ n * (1 - n) // 2] + list(range(1, n))