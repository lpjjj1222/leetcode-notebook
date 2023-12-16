class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        #第一个孩子可能得到的糖果数i  min(n,limit)
        #第二个孩子可能得到的糖果数j   min(n-i,limit)
        #第三个孩子可能得到的糖果数k  n-i-j
        count = 0
        for i in range(min(n,limit)+1):
            for j in range(min(n-i,limit)+1):
                k = n-i-j
                if k >=0 and k <=limit:
                    count += 1
        return count
        
