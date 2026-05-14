class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        length = len(num)
        num.sort()
        left = right = ''
        
        for i in range(length):
            if i % 2 == 0:
                right += num[i]
            else:
                left += num[i]
        
        return int(left) + int(right)