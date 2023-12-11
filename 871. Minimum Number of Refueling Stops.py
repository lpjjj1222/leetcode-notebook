class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:    
        #dp[j]表示加了j次油，能行驶到的最远距离 
        dp = [0] * (len(stations)+1)

        dp[0] = startFuel#(加了0次油，最远距离就是startFuel)

        for i in range(len(stations)): #一个个加油站遍历(物品)
            for j in range(i,-1,-1): #加油次数 （背包容量）
                if dp[j] >= stations[i][0]:#如果加j次油能到达该station，就可以考虑是否在这station加油
                    #如果在该站加，则dp[j+1] = dp[j]+station[i][1]
                    #否则，不更新
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])

        #如果每个加油站都加了还是去不到target..            
        if dp[-1] < target:
            return -1
        
        #要找加油次数最少则从左往右找第一个dp值大于等于target的:
        for i in range(len(dp)):
            if dp[i] >= target:
                return i


        



                






       
       


        

        
