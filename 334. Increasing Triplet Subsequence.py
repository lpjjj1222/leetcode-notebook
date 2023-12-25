class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small_1 = small_2 = float('inf')
        for n in nums:
            if n <= small_1:
                small_1 = n
            elif n <= small_2:
                small_2 = n
            else:
                if small_1 != float('inf') and small_2 != float('inf'):
                    return True
        return False



        
