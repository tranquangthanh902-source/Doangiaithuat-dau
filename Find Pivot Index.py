class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        
        # B2: Duyệt qua từng chỉ số i
        for i in range(len(nums)):
            # Tính tổng bên phải dựa trên tổng tổng quát và tổng bên trái
            right_sum = total_sum - left_sum - nums[i]
            
            # Kiểm tra điều kiện đề bài
            if left_sum == right_sum:
                return i
            
            # Cập nhật left_sum để dùng cho vòng lặp tiếp theo
            left_sum += nums[i]
            
        # Nếu không tìm thấy pivot index nào
        return -1