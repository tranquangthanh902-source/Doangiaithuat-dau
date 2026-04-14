class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Duyệt từ cuối mảng lên đầu
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # Nếu chữ số < 9, cộng 1 và xong luôn
                digits[i] += 1
                return digits
            
            # Nếu là 9, biến nó thành 0 và tiếp tục vòng lặp để cộng nhớ vào số trước
            digits[i] = 0
            
        # Nếu chạy hết vòng lặp mà chưa return, nghĩa là mảng toàn số 9 ban đầu
        # Ví dụ: [9, 9] -> sau vòng lặp thành [0, 0]. Ta cần thêm 1 vào đầu thành [1, 0, 0]
        return [1] + digits 