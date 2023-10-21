class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 0:
            return result

        col_begin = 0
        col_end = len(matrix[0]) - 1
        row_begin = 0
        row_end = len(matrix) - 1

        total_n = len(matrix[0]) * len(matrix)

        while row_begin <= row_end and col_begin <= col_end:  
            if len(result) < total_n: 
                for j in range(col_begin,col_end+1):
                    result.append(matrix[row_begin][j])
                row_begin += 1
            if len(result) < total_n: 
                for i in range(row_begin,row_end+1):
                    result.append(matrix[i][col_end])
                col_end -= 1
            if len(result) < total_n: 
                for j in range(col_end, col_begin-1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1
            if len(result) < total_n: 
                for i in range(row_end, row_begin-1 , -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1
        return result  
