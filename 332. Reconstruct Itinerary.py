#这个是我自己写的，过了前80个Case 过不了最后一个 超时了
#代码随想录的前两个答案也超时，只有那个用字典的不超时

'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.result = []
        tickets.sort()
        used = [False] * len(tickets)
        self.backtracking(['JFK'],used,tickets)
        return self.result

    def backtracking(self, path, used, tickets):
        if len(path) == len(tickets) + 1:
            self.result = path
            # print('可以了')
            return True

        for index, ticket in enumerate(tickets):
            if used[index] == False and tickets[index][0] == path[-1]:
                #找没用过的机票且对得上上一个地方的
                path.append(tickets[index][1])
                used[index] = True
                #向下递归
                # print('path is',path)
                # print('used is',used)
                # print('继续递归')
                if self.backtracking(path, used, tickets):
                    return True
            
                path.pop()
                used[index] = False
        return False
'''

#代码随想录里的字典解法
#这道题看着这个Case来想就行了
#ticket = [[“jfk”，“kul”],["nrt","jfk"],["jfk","nrt"]]
class Solution:
    from collections import defaultdict
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = defaultdict(list)
        for ticket in tickets:
            targets[ticket[0]].append(ticket[1])
        #以上得到字典，key是出发地，value是一个list,list里装的是目的地

        for value in targets.values():
            value.sort(reverse=True)
        #以上将Targets字典中的目的地按照逆序排序

        self.result = []
        self.backtracking("JFK", targets)
        return self.result[::-1] #return result (逆序)
    
    def backtracking(self, start, targets):
        while targets[start]:  #当某个出发机场有目的机场时
            next_start = targets[start].pop() #找到下一个出发机场 并在targets里把用过的目的地去掉
            self.backtracking(next_start, targets)
        self.result.append(start) #当某个出发机场找不到目的机场时，放进result里
        #result最后是要逆序返回的 belike jfk-nrt-jfk-kul 在result里是["kul"<-"jfk"<-"nrt"<-"jfk"]
        #所以找不到出发机场的kul会最先进result,因为他左边没有东西了





        












