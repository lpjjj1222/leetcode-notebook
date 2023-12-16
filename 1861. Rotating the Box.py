class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        #STEP1：把石头向右边移
        for i in range(len(box)):
            stone = 0
            for j in range(len(box[0])):
                if box[i][j] == "#":#如果是石头
                    stone += 1
                    box[i][j] = "."
                elif box[i][j] == "*":#如果是obstacle，就在obstacle紧邻的左边开始往左放本来在左边的所有石头
                    for s in range(stone):
                         box[i][j-s-1] = "#"
                    stone = 0 #排布完后归零
            #STEP2:遍历到最右边，还有石头，即如果最后一块obstacle的右边还有石头，就需要从盒子最右边开始往左排剩下的石头
            if stone > 0:
                for s in range(stone):
                    box[i][j-s] = "#"
        #将矩阵向右旋转90°
        #box[::-1]将最后一行变成第一行，行反转
        #*box[::-1]的*解包，将每行作为独立的参数传递给zip
        #zip()将每个参数同一位置的元素打包成元组
        #赋值给box[:],原本每一行变成了一个个元组，由于box[:],会变成和原来一样的数据类型变回列表
        
        box[:] = zip(*box[::-1])
        return box
        
