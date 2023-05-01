class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row = 0
        column = 0
        #创建一个 n * n 的列表，即列表里有n个列表，且每个列表里有n个元素

        #使用[0] * 10会导致10个子列表共享同一个列表对象，所以修改一个子列表中的元素会影响其他子列表中对应位置的元素。
        #要避免这个问题，可以使用循环来逐个生成子列表
        res = [[0] * n for _ in range(n)]


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



        #大神解法：
        '''
        def generateMatrix(self, n):
            A = [[0] * n for _ in range(n)] #这一步一样，都是创建一个全是0的列表
            i, j, di, dj = 0, 0, 0, 1   #i是行数 j是列数 
                                        #di可以理解为下一步的行数变量or方向 dj同理 
            for k in range(n*n):
                A[i][j] = k + 1   #填入数字，k+1是因为range是每一个小1 总之填入的是k+1

                if A[(i+di)%n][(j+dj)%n]:  #判断是否转弯 
                                           #i+di 和 j+dj是下一个格子的坐标
                                           # 行列数要%n是因为转弯有两种可能性
                                           #一种是下一个格子已经被填过数了
                                           #另一种是下一个格子超出界限了
                                           #比如4*4的格子 填完4再向右的时候
                                           #坐标就超出界限了
                                           #这时用%n就可以把判断条件符合界限内

                    di, dj = dj, -di     #这个改变方向的东西也很屌
                i += di
                j += dj
            return A
        '''
