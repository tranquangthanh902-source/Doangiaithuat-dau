class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import Counter
        d = Counter(a + b for a in nums1 for b in nums2)
        return sum(d[-(c + d2)] for c in nums3 for d2 in nums4)