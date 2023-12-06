class UnionFind:
    def __init__(self, N):
        self.root = [-1] * N
        for i in range(N):
            self.root[i] = i
    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            return self.find(self.root[x])
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootX] = rootY

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        ownership = {} #key 是email, value是owner

        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership: #如果已经被登记了，就是其实已经有主人了，这是主人重复的号
                    uf.union(i, ownership[email])
                #如果邮箱没见过，直接添加 (见没见过都加进ownership因为后面会找出)
                ownership[email] = i
        print(ownership)
        print(uf.root)
            
        result = collections.defaultdict(list)
        for email, owner in ownership.items(): #作为根节点的owner登记就行
            print(owner,"根节点是",uf.find(owner))
            result[uf.find(owner)].append(email)
        # print(result)

        return [[accounts[i][0]] + sorted(emails) for i, emails in result.items() ]


            


        
