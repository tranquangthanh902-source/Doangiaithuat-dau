class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # B2: Duyệt qua chuỗi s
        for i in range(n):
            # Lấy giá trị hiện tại
            current_val = roman_map[s[i]]
            
            # Kiểm tra xem có phần tử tiếp theo không và so sánh
            if i + 1 < n and current_val < roman_map[s[i+1]]:
                # Quy tắc trừ: Nếu nhỏ hơn số đằng sau
                total -= current_val
            else:
                # Quy tắc cộng: Nếu lớn hơn hoặc bằng số đằng sau
                total += current_val
                
        return total