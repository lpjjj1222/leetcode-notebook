        #这个方法里的nums.pop()是O(N)的操作，因为没pop(i)一次就要把i后面的元素向前移动 因此整个算法的复杂度是O(m*n),n是零的个数，pop几次零， m是整个数组的长度，遍历一遍数组
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        zeros = 0
        size = len(nums)
        while i < size-zeros:
            if nums[i] == 0:
                zeros += 1
                nums.append(0)
                nums.pop(i)
            else:
                i += 1
'''
#快慢双指针，通过两两交换而非pop()和append()降低了时间复杂度，时间复杂度O(N),空间复杂度O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[last_non_zero], nums[cur] = nums[cur], nums[last_non_zero]
                last_non_zero += 1
        

    




                
            
                

            


        
