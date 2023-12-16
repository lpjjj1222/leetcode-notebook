'''
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        supply = set(supplies)
        dq = deque([(r,ing) for r, ing in zip(recipes, ingredients)])
        #遍历(r,ing)看能否把r即recipes做出来，如果可以，则将recipes放进ans,同时放进supply。
        #如果ingredients不全，则把(r,ing)放在队列末端，等待下一圈重新遍历
        #遍历完一圈后如何判断是否需要遍历下一圈？ 如果supply增加了，就再遍历一圈
        supply_size = len(supply)
        new_supply_size = -1
        while supply_size != new_supply_size:
            supply_size = len(supply)
            dq_size = len(dq)

            for _ in range(dq_size):
                r,ing = dq.popleft()
                can_cook = True
                for i in ing:
                    if i not in supply:
                        can_cook = False
                        break
                if can_cook == True:
                    ans.append(r)
                    supply.add(r)
                else:
                    dq.append((r,ing))
            new_supply_size = len(supply) 
        return ans
'''


#拓扑排序法（用于处理具有依赖关系的情景）
#首先标记出那些可以立即制作的食谱，然后，更新依赖于这些食谱的其他食谱的状态。这个过程类似于在有向图中移除已经处理过的节点，并检查这些操作是否使得其他节点（食谱）现在可以处理。
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        supply = set(supplies)
        count_unfinish = Counter()
        #STEP1: 同时遍历recipes和ingredients, 记录每个暂时没有的食材contribute to 哪些recipe，用defaultdict(set)记录，同时看每个recipe是否能做出来，如果能做出来则直接添加到ans,如果不能则把lack_count +1，记录该recipe缺多少食材。这个lack_count 存在count_unfinish里
        ingredient_recipe = defaultdict(set)
        for ingredient,rcp in zip(ingredients, recipes):
            lack_count = 0
            for ing in ingredient:
                if ing not in supply:
                    lack_count += 1
                    ingredient_recipe[ing].add(rcp)
            if lack_count == 0:
                ans.append(rcp)
            else:
                count_unfinish[rcp] += lack_count
        #STEP2:把做好的ans里的rcp搬出来看看哪些recipe当时需要这个rcp作为ingredients（一个for循环遍历list,利用list的可变性）
        for rcp in ans:
            print("做好的：",rcp)
            for recipe in ingredient_recipe.pop(rcp, set()): #将ingredient_recipe这个字典里rcp作为键的value提取出来，value是集合，集合里是一个个未完成的recipe，如果找不到集合出来则返回空的集合set()
                count_unfinish[recipe] -= 1
                if count_unfinish[recipe] == 0:
                    ans.append(recipe)
                #不用担心burger需要sandwich而sandwich需要bread的三层关系而一个for循环无法解决，这里刚好就是用了list的可变性！   
        return ans
        


            

        



        
            
        
