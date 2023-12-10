class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #step1:以对角线为轴交换
        #step2:以中间竖着的一列为轴交换

        #step1:
        n = len(matrix[0])
        start = 1
        for i in range(0, n): #0 1 2 3  
            for j in range(start,n): # 1  2 3
                matrix[i][j], matrix[j][i] = matrix[j][i] , matrix[i][j]
            start += 1
        
        #step2:

        for row in matrix:
            left = 0
            right = n-1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
        print(matrix)

        
