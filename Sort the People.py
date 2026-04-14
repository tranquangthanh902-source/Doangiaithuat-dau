class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = zip(heights , names)
        people = sorted(people , reverse=True)
        return [name for height,name in people]