class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Điều kiện dừng: nếu mảng có 1 phần tử hoặc rỗng
        if len(nums) <= 1:
            return nums
        
        # Chia mảng thành 2 nửa
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # Trộn (merge) 2 nửa đã sắp xếp
        return self.merge(left_half, right_half)

    def merge(self, left, right):
        res = []
        i = j = 0
        
        # So sánh và nhặt phần tử nhỏ hơn
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        # Thêm các phần tử còn lại (nếu có)
        res.extend(left[i:])
        res.extend(right[j:])
        
        return res