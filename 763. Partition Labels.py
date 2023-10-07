class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        

        last_occurance = {} #创建字典，统计每个字母最后出现的位置
        for index, letter in enumerate(s):
            last_occurance[letter] = index

        end = 0
        count = 0
        for i in range(len(s)):
            count += 1
            end = max(last_occurance[s[i]],end)
            if i == end:#遍历到end了
                result.append(count)
                count = 0
                end = 0
        return result
        
        
        
