class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = dict()
        result = []
        array = [0] * numCourses
        q = deque()
        for record in prerequisites:
            array[record[0]] += 1
            if record[1] not in dic:
                dic[record[1]] = list()
                dic[record[1]].append(record[0])
            else:
                dic[record[1]].append(record[0])

        for i in range(numCourses):
            if array[i] == 0:
                q.append(i)
        while q:
            c = q.pop()
            result.append(c)
            if c in dic:
                for cc in dic[c]:
                    array[cc] -= 1
                    if array[cc] == 0:
                        q.append(cc)
        if len(result) < numCourses:
            return []
        return result

        
