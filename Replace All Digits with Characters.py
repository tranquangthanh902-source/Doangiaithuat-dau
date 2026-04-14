class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        for i in range(1, len(a), 2):
            a[i] = chr(ord(a[i - 1]) + int(a[i]))
        return ''.join(a)