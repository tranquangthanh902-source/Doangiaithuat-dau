class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
            
        n = len(haystack)
        m = len(needle)
        
        # Duyệt qua haystack, chỉ cần duyệt đến n - m + 1
        for i in range(n - m + 1):
            # So sánh chuỗi con của haystack với needle
            if haystack[i : i + m] == needle:
                return i
                
        # Nếu duyệt hết mà không thấy
        return -1