#字典1
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = collections.defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        return max(num_dict.keys(),key = num_dict.get)
'''
#字典2
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = collections.Counter(nums) #返回一个字典，key是元素，value是出现的次数
        print(num_dict)
        return max(num_dict, key=num_dict.get) #注意取最大值跟上面字典1不一样
'''
#将nums由小到大排列，因为majority element出现次数> (n/2)所以长度为奇数的nums找索引n//2即可，长度为偶数的nums找索引n//2也可
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
'''

# Boyer-Moore 投票算法
class Solution:
    def majorityElement(self, nums:List[int]) -> int:
        #让第一个元素作为majorityElement的候选，count = 1
        #一个个遍历，如果又遇到该候选，则count += 1,否则count-=1
        #当count = 0 时，让此时遍历的元素作为候选majorityElement并且count=1
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count = 1
        
        return candidate





        
