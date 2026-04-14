class Solution(object):
    def checkValid(self, matrix):
       
        n = len(matrix)
        expected = set(range(1, n + 1))

        for row in matrix:
            if set(row) != expected:
                return False

        for col in zip(*matrix):
            if set(col) != expected:
                return False

        return True