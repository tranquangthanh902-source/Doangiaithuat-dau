class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', number))