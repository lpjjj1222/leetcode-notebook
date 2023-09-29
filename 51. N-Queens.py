#皇后不打架的意思是：同一行同一列以及45度不能有一个以上的皇后
#这道题是看了代码随想录看到“代码实现”，Carl讲完要用什么参数之后自己写出来哒
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.backtracking(n, [], 0)
        return self.result
    
    def backtracking(self, n, chessboard, row):
        if row == n:
            self.result.append(list(chessboard))
            return
        
        for index in range(0,n):
            if self.isvalid(n, chessboard,row, index) == True: #判断该棋盘该位置是否能放皇后
                level = ["."] * n
                level[index] = "Q"
                level = "".join(level)
                chessboard.append(level)
            else:
                continue
            
            print('now chessboard is', chessboard)
            self.backtracking(n, chessboard, row+1)

            chessboard.pop()

    def isvalid(self, n, chessboard, row, index):
        for i, level in enumerate(chessboard): #i是行数， level是这一行的内容
            if level[index] == "Q": #检查每一行，如果有某一行的第index列有Q则返回False
                return False

            if index - (row-i) >= 0 and level[index - (row-i)] == "Q": #检查对角线 ，详细解释看下面注释
                return False
            if index + (row-i) < n and level[index + (row-i)] == "Q":
                return False

            #检查上面几层的对角线上是否有Q，有则返回False
            #如何找上面几层对角线的坐标呢？
            #例如找（3,2）对应的对角线坐标，向左上找的话
            #第二层(2, *) 的*就可以2 -（3-2），即 * = index - (row - i)
            #向右上找的话，第二层(2,#)的#就可以2+(3-2),即(2,3) 即# = index + (row-i)
            #所以，对每一层i来说，去找level[i-(row-index)] ,看看是否为"Q"就行
        return True

  





        
