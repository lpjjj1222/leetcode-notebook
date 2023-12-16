class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count = 0
        dic = collections.Counter()
        distinct_num = len(set(nums))

        while right < len(nums):

            dic[nums[right]] += 1
                #此时left-right已经组成了满足条件的子数组，因此，以left开头，以right和right后面任意数结尾的数组都符合
                #试着把left往右推，看看是否依旧满足
            while len(dic) == distinct_num:
                count += len(nums)- right

                dic[nums[left]] -= 1
                if dic[nums[left]] == 0:
                    del dic[nums[left]]
                left += 1
                
            right += 1
        return count
                




        
