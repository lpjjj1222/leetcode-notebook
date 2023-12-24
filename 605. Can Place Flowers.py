class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_f = 0
        for i, f  in enumerate(flowerbed):
            if i == 0 and f == 0:
                if len(flowerbed) == 1:
                    max_f += 1
                elif flowerbed[i+1] == 0:
                    max_f += 1
                    flowerbed[i] = 1
            elif i > 0 and f==0:
                if flowerbed[i-1] == 0:
                    if i == len(flowerbed)-1:
                        max_f += 1
                    elif flowerbed[i+1] == 0:
                        max_f += 1
                        flowerbed[i] = 1
        
            
        return max_f >= n
            


        
