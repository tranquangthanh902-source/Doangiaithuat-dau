class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height) - 1
        mostWater = 0

        while start < end:
            w = end - start
            h = min(height[start], height[end])

            mostWater = max(mostWater, w * h)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return mostWater
        