class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        current_ones = 0
        
        for n in nums:
            if n == 1:
                # Nếu thấy số 1, tăng biến đếm hiện tại
                current_ones += 1
            else:
                # Nếu thấy số 0, cập nhật kỷ lục và reset biến đếm
                if current_ones > max_ones:
                    max_ones = current_ones
                current_ones = 0
        
        # Sau khi hết vòng lặp, cần so sánh lần cuối 
        # (phòng trường hợp chuỗi số 1 nằm ở cuối mảng)
        return max(max_ones, current_ones)