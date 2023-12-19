class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_list = []
        res = 0
        for interval in intervals:
            print(interval)
            if not end_list:
                res += 1
                end_list.append(interval[1])
            else:
                add_room = True
                for i,end in enumerate(end_list):
                    if interval[0] >= end: #结束后才开始，不用加房间
                        end_list[i] = interval[1]
                        add_room = False
                        break
                    else: #结束前开始，继续遍历，如果在所有结束前开始，才加
                        continue
                if add_room == True:
                    end_list.append(interval[1])
                    res += 1
        return res

                
            
