#这道题先把代码随想录的视频看完吧
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)
        
    def backtracking(self, board):
        for i in range(0,len(board)): #i是行
            for j in range(0, len(board)):  #j是列
                if board[i][j] == ".": #遇到空格才需要处理
                    for k in range(1,10):
                        if self.isvalid(k, i, j, board) == True:
                            board[i][j] = str(k) #放入valid的数进空格
                            result = self.backtracking(board) #递归，看下一个空格（再走一次两个for loop找空格）
                            if result == True:
                                return True

                            board[i][j] = "." #回溯
                   
                    return False #如果1-9每个数都遍历了，都不能放进那个空格，就要return False
        return True #如果说所有都填满了或者本来给的数独题目就是填满的，直接返回True

    def isvalid(self, k, i, j, board):
        k = str(k)
        if k in board[i]: #如果k已经存在这一行了
            return False
        for row in board: #遍历每一行，看看这一列会不会已经有k了
            if row[j] == k:
                return False
        def location(number):
            if number in range(0,3):
                return 0
            elif number in range(3,6):
                return 3
            elif number in range(6,9):
                return 6
        location_i = location(i)
        location_j = location(j)
        for ii in range(location_i, location_i + 3):
            for jj in range(location_j, location_j + 3):
                if board[ii][jj] == k:
                    return False
        return True            
        
        


        
