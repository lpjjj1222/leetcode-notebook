class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #中间状态
        #0-死-死
        #1-活-活
        #2-活-死
        #3-死-活
        
        #先遍历第一遍，将所有的格子变为中间状态
        #中间状态对0 1 的设置跟原来一样所以不影响判断
        #因此，邻居是0或3都是死
        #邻居是1或2都是活
        rows, cols = len(board), len(board[0])
        def checkNeig(r,c):
            lives = 0
            #遍历[i,j]所在行列和上下两行和左右两列
            for i in range(max(0,r-1), min(r+2,rows)):
                for j in range(max(0,c-1),min(c+2,cols)):
                    if r == i and c == j:
                        continue
                    if board[i][j] in [1,2]:
                        lives += 1
            return lives

        for i in range(rows):
            for j in range(cols):
                lives = checkNeig(i,j)
                if board[i][j] == 1 and (lives < 2 or lives >3):#活-死
                    board[i][j] = 2
                elif board[i][j] == 0 and lives == 3: #死-活
                    board[i][j] = 3 
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1 
               


        
