class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            pass
        else:
            for x in range(0, n//2):
                for y in range(x, n-1-x):
                    matrix[y][n-x-1], matrix[n-x-1][n-y-1], matrix[n-y-1][x], matrix[x][y] = \
                    matrix[x][y], matrix[y][n-x-1], matrix[n-x-1][n-y-1], matrix[n-y-1][x]



        