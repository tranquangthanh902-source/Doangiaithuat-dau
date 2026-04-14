class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        count = [0] * 46
        max_count = 0

        for num in range(lowLimit, highLimit + 1):
            digit_sum = 0
            temp = num
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            count[digit_sum] += 1
            max_count = max(max_count, count[digit_sum])

        return max_count