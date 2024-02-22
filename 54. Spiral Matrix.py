class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        Ncol = len(matrix[0])
        Nrow = len(matrix)
        rounds = math.ceil(len(matrix) / 2)
        res = []
        nums = Ncol * Nrow
        print(matrix)
        

        for rd in range(rounds):
            #第rd行从左向右，[rd:Ncol-rd]
            for j in range(rd, Ncol-rd):
                res.append(matrix[rd][j])
            if len(res) == nums:
                break
            #第rd+1行开始到Nrow-rd行结束的每一行的倒数第rd个
            for i in range(rd+1, Nrow-rd):
                res.append(matrix[i][Ncol-rd-1])
            if len(res) == nums:
                break
            #第Nrow-rd-1行从右向左，[Ncol-rd-2:rd-1,-1]
            for j in range(Ncol-rd-2, rd-1,-1):
                res.append(matrix[Nrow-rd-1][j])
            if len(res) == nums:
                break
            
            #第Nrow-rd-1行开始到rd+1行结束的每一行的第rd个
            for i in range(Nrow-rd-2, rd,-1):
                res.append(matrix[i][rd])
            if len(res) == nums:
                break
        return res



        
