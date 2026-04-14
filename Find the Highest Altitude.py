class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cur = 0
        maxnum = 0
        
        for i in gain:
            cur += i
            maxnum = max(cur, maxnum)
        return maxnum 