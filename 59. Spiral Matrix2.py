class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row = 0
        column = 0
        #创建一个 n * n 的列表，即列表里有n个列表，且每个列表里有n个元素

        #使用[0] * 10会导致10个子列表共享同一个列表对象，所以修改一个子列表中的元素会影响其他子列表中对应位置的元素。
        #要避免这个问题，可以使用循环来逐个生成子列表
        res = list()
        for _ in range(n):
            sublist = [0] * n
            res.append(sublist)

        def right(row,column,num,end,small):
            if num > n*n:
                return res
            res[row][column] = num

            if column < end:
                return right(row,column + 1,num + 1,end,small)
            else:
                return down(row + 1,column,num + 1,end,small)

            
            
        def down(row,column,num,end,small):
            if num > n*n:
                return res
            
            res[row][column] = num

            if row < end:
                return down(row+1,column,num + 1,end,small)
            else:
                return left(row,column - 1,num + 1,end,small)

            
            
        def left(row,column,num,end,small):
            if num > n*n:
                return res
            
            res[row][column] = num
            

            if column > small:
                return left(row,column - 1,num + 1,end,small)
            else:
                return up(row - 1,column,num + 1,end,small + 1)

            
            
        def up(row,column,num,end,small):
            if num > n*n:
                return res
            
            res[row][column] = num
            


            if row > small:
                return up(row - 1,column,num + 1,end,small)
            else:
                return right(row,column + 1,num + 1,end - 1,small)


        return right(0,0,1,n - 1,0)
