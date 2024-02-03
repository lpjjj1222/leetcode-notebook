class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        #暴力解法是两个for循环，spells顺序不能变，必须从左到右遍历，但是potions可以不按顺序，所以可以先给potions排序然后用二分法
        result = []
        potions.sort()
        for spell in spells:
            res = 0
            left = 0
            right = len(potions)-1
            while left <= right:
                mid = left + (right-left) // 2
                if potions[mid] * spell >= success: #已经符合了，所以mid右边的都ok
                    res += right - mid + 1
                    right = mid - 1
                elif potions[mid] * spell < success: #还不符合，那么mid左边的就更不行了
                    left = mid + 1
            result.append(res)
        return result



        
