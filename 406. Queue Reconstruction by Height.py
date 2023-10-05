#这道题直接看代码随想录的解法和思考过程
#关键点：先确定身高的维度，再确定k维度
#把身高从高到矮排好后，可以保证身高矮的在队列的后面，这样根据k调整的时候，我们把后面的插入到前面就不会影响被插队的状况
#因为其实被插队的人只会考虑前面比他高的人，但是拿一个矮子插队，并不会影响

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #根据身高从大到小排列 
        #当身高一样的时候，k小的排在前面（举个例子就知道）
        #为了达到上面这句的目的，应该先把整个people按照k从小到大排，然后再按身高从大到小排
        #不然直接排身高的话，有的时候身高一样k小的在前面，有的时候k大的在前面
        people.sort(key = lambda x: x[1])
        people.sort(key = lambda x: x[0],reverse = True)
        for now_index, person in enumerate(people):
            future_index = person[1]
            people.pop(now_index)
            people.insert(future_index, person)
        return people


        
