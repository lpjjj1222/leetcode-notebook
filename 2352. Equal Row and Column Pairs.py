#BETTER！！！！！
#下面的方法使用hash table加速， 由于list不能作为字典的key,因为key要求不可变，所以要转化为tuple
#时间复杂度:O(N的平方)
#空间复杂度: O(N的平方)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = defaultdict(int)
        cols = list(zip(*grid))
        res = 0
        for row in grid:
            dic[tuple(row)] += 1
        for col in cols:
            if col in dic:
                res += dic[col]
        return res

#cols = [list(x) for x in zip(*grid)] O(N的平方)其中N是矩阵的维度，（N * N的矩阵）
#由于两层for循环而且执行的语句是O(N)，（因为需要比较完一整行和一整列才能知道是否相等
#所以时间复杂度是O(N的三次方)
#空间复杂度：由于将列提取出来变成列表，需要创造n个长度为n的列表，所以为O(N的平方)
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = [list(x) for x in zip(*grid)]
        res = 0
        for col in cols:
            for row in grid:
                if col == row:
                    res += 1
        return res
'''





        
