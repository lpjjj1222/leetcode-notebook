class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_top = 0
        row_bottom = len(matrix) - 1

        while row_top < row_bottom:
            matrix[row_top], matrix[row_bottom] = matrix[row_bottom], matrix[row_top]
            row_top += 1
            row_bottom -= 1
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
        
