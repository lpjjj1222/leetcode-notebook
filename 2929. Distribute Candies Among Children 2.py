#下面这个方法用了循环嵌套，超时了！！
'''
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        #第一个孩子最少要分: max(n-2*limit,0)，最多能分: min(limit, n)
        #第二个孩子最少要分：max(n-i-limit, 0), 最多能分: min(limit,n-i)

        count = 0
        min_1 = max(n-2*limit,0)
        max_1 = min(limit,n)

        for i in range(min_1,max_1+1):
            min_2 = max(n-i-limit,0)
            max_2 = min(limit,n-i)
            for j in range(min_2,max_2+1):
                k = n-i-j
                if k >=0 and k <=limit:
                    count += 1
        return count
'''

class Solution:
        def f(self,n,L):#用来计算分了第一个孩子后，第二个孩子的可能数（不用算第三个，因为前两个确定了，第三个孩子的数肯定是一样的）
            min_candy = max(n-L,0) #比如还剩6🍬，L=3，不能给第二个分2🍬
            max_candy = min(n,L)
            #如果min_candy > max_candy，即第一个孩子分的糖果数有问题，则return 0 (eg.10🍬，limit=3,第一个分0🍬)        
            return max(0,max_candy-min_candy+1)

        def distributeCandies(self, n: int, limit: int) -> int:
            count = 0
            
            for i in range(min(n,limit)+1):#第一个孩子分的🍬
                count += self.f(n-i,limit)
            return count




      
    
        




        
