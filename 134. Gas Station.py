class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        effect = [z-c for z,c in zip(gas,cost)]
        start = 0
        cur = 0
        i = 0
        #先判断总的effect是否大于0,防止出现[-1,-1,1]这种，下面的循环无法检测
        if sum(effect) < 0:
            return -1 


        for i in range(len(effect)):
            cur += effect[i]
            if cur < 0 and i + 1 < len(gas):
                start = i + 1
                cur = 0
        if cur >= 0: 
            return start
        return -1
            

        