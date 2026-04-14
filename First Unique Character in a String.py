class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        
        # Bước 1: Đếm số lần xuất hiện của mỗi ký tự
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Bước 2: Duyệt lại chuỗi để tìm ký tự đầu tiên có count == 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
                
        # Nếu duyệt hết mà không thấy ký tự nào duy nhất
        return -1