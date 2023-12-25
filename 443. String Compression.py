class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0 #用来一点点更新答案的
        
        while i < len(chars):
            group_l = 1
            while group_l + i < len(chars) and chars[group_l+i]==chars[i]:
                group_l += 1
            chars[res] = chars[i]
            res += 1
            if group_l > 1:
                res_num = str(group_l)
                chars[res:res+len(res_num)] = list(res_num)
                res += len(res_num)
            i += group_l
        return res
            




                



            

        
        
