class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Nrow = len(matrix)
        Ncol = len(matrix[0])
        #首先先看原始matrix的第0列是否有0，如果有，最后是要把一整个第0列刷为0的
        iscol0 = False
        for i in range(Nrow):
            if matrix[i][0] == 0:
                iscol0 = True
        #第一遍，除了第0列，一个个遍历，如果为0，就把所在行首和列首置0
        #第二遍，遍历第0列和第0行的每一个元素，如果有0，就把第0列所在的行刷为0，([0,0]作为列元素判断),把第0行所在的列刷为0

        #第一遍
        for i in range(Nrow):
            for j in range(1,Ncol):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0 , 0        
        
        #第二遍看的时候不看[0,0]，因为如果看了[0,0]就有可能把第一行和第一列全部搞成0，那整个matrix都变成0了！最后再看
        #先看第0列，从[1,0]开始
        for i in range(1,Nrow):
            if matrix[i][0] == 0:
                for j in range(Ncol):
                    matrix[i][j] = 0

        #再看第0行，从[0,1]开始
        for j in range(1,Ncol):
            if matrix[0][j] == 0:
                for i in range(Nrow):
                    matrix[i][j] = 0

        #先看[0,0]再看要不要把第0列刷0，不然，如果先刷第0列，即使[0,0]不为0，也会被刷0，然后就把第0行也刷成0了
        if matrix[0][0] == 0:
            for j in range(Ncol):
                matrix[0][j] = 0

        if iscol0 == True:
            for i in range(Nrow):
                matrix[i][0] = 0

        return matrix
                            
        
        
