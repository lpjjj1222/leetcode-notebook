class Solution(object):
    
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(board)
        n = len(board[0])
        done = True

        for r in range(m):
            for c in range(n-2):

                num1 = abs(board[r][c])

                num2 = abs(board[r][c+1])

                num3 = abs(board[r][c+2])

                if num1 == num2 and num2 == num3 and num1 != 0:
                    done = False

                    board[r][c] = -num1

                    board[r][c+1] = -num2

                    board[r][c+2] = -num3

        for c in range(n):
            for r in range(m-2):

                num1 = abs(board[r][c])

                num2 = abs(board[r+1][c])

                num3 = abs(board[r+2][c])

                if num1 == num2 and num2 == num3 and num1 != 0:

                    done = False

                    board[r][c] = -num1

                    board[r+1][c] = -num2

                    board[r+2][c] = -num3

        # gravity, crash dow

        for c in range(n):

            index = m - 1

            for r in range(m-1, -1, -1):

                if board[r][c] > 0:

                    board[index][c] = board[r][c]

                    index -= 1

            for r in range(index, -1, -1):

                board[r][c] = 0

        return board if done == True else self.candyCrush(board)















                

                

            
                

