class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = defaultdict(int)
        for letter in s:
            dic[letter] += 1
        dic = dict(dic)
        
        dic_letter = sorted(dic.keys(),key = lambda x: dic[x], reverse = True)
        top = dic_letter[0]

        if dic[top] * 2 > len(s)+1:
            return ""

        index = 0
        res = [""] * len(s)
        for letter in dic_letter:
            for _ in range(dic[letter]):
                if index >= len(s):
                    index = 1
                res[index] = letter
                index += 2
        return "".join(res)


            



        
        
