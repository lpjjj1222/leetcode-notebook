class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort( reverse = True)  #从大到小遍历
        s.sort(reverse = True) #从大到小遍历
        number_content = 0
        index = 0  #index饼干的下标
        for child_greed in g: #遍历一个个孩子的胃口
            if index <= len(s) - 1 and s[index] >= child_greed:
                index += 1
                number_content += 1
     
        return number_content



        
