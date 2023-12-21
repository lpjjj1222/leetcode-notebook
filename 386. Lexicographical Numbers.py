
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1

        for _ in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur == n: #n=100, 100 -> 11  & n = 192, 192 -> 2
                    cur = cur // 10
                cur += 1 #n = 13, 12 -> 13

                #除去多余的0，eg.n = 192, 192 -> 2, 192//10 +1 = 20,然而应该从2开始而非20开始
                while cur % 10 == 0:
                    cur = cur // 10
        return res

        
            


        
