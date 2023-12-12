



        
class Solution:
    #STEP1:(i,j)右下角，(x,y)左上角，找该矩阵的累加和,如果都没有X，即累加和为0，则可以放一整张邮票
    def prefixSum(self, grid):
        m , n = len(grid), len(grid[0])
        prefix_sum = [[0] * (n+1) for _ in range(m+1)]
        #n+1和m+1是因为后面递推公式有i-1,j-1

        #在prefix_sum二维数组中，（i-1,j-1)对应grid的(m,n)
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + grid[i-1][j-1]
        return prefix_sum
    def sumRegion(self,prefix_sum, x,y,i,j):
        #(x,y)为原格子的左上角，(i,j)为原格子的右下角
        return(prefix_sum[i+1][j+1]-prefix_sum[i+1][y]-prefix_sum[x][j+1]+prefix_sum[x][y])
    
    def possibleToStamp(self, grid, H, W):
        prefix_sum = self.prefixSum(grid)
        m , n = len(grid), len(grid[0])
        valid_right_bottom_board = [[0] * n for _ in range(m)]
        for i, j  in product(range(m),range(n)):
            if i-H+1>= 0 and j-W+1 >=0:
                if self.sumRegion(prefix_sum,i-H+1,j-W+1,i,j)==0:
                    valid_right_bottom_board[i][j] = 1
        print(valid_right_bottom_board)
        
        
        #STEP2:遍历每一个非X的格子看能否被邮票覆盖
        prefix_sum = self.prefixSum(valid_right_bottom_board)
        for x, y in product(range(m),range(n)):#(x,y)为左上角，右下角的格子为(x+H-1,y+W-1)
            if grid[x][y] == 0: #如果该格子是非X，才要看他是否是能被覆盖
                if x+H-1>m-1:
                    i = m-1
                else:
                    i=x+H-1
                if y+W-1> n-1:
                    j = n-1
                else:
                    j = y+W-1
                if self.sumRegion(prefix_sum,x,y,i,j)>0:
                    continue
                else:
                    return False
        return True
        

        
        


            
        
