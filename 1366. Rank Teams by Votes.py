#创建一个字典，key是每个Team，value是每个Team被排名的频率
#d['A'] = [3, 0, 1] 指TeamA 被排在第一3次，第二0次，第三1次，对字典的键进行排序，就会自动按照value的第一位，第二位。。。这样排，如果第一位相同自动看第二位这样

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = dict()
        rank_list = list(zip(*votes))
        team_num = len(votes[0])

        for rank,team_list in enumerate(rank_list):
            for team in team_list:
                if team not in d:
                    d[team] = [0] * team_num
                    d[team][rank] += 1
                else:
                    d[team][rank] += 1
        print(d)
        rank_name = sorted(d.keys())
        rank_rank = sorted(rank_name,key = lambda x:d[x],reverse=True)
        return "".join(rank_rank)
        


                


        
