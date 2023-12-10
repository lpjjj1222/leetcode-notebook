class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
                #https://www.bilibili.com/video/BV1Wt411Y7Y9/?spm_id_from=333.337.search-card.all.click&vd_source=d4c5dda6ddeb9c685d0c362baa1edb3e 看这个视频
        #将task按照频率从高到低排序，最高频率的作为主要间隔，假设最高频率的task为A，其频率为k,一共有p种task跟A频率一样（包括A）
        fre_dict = [0] * 26
        for task in tasks:
            fre_dict[ord(task)-ord('A')] += 1
        fre_dict.sort(reverse=True)

        max_frequency = fre_dict[0]
        count = 0
        for f in fre_dict:
            if f == max_frequency:
                count+=1
        result = (max_frequency-1) * (n+1) + count
        if result < len(tasks):
            return len(tasks)
        else:
            return result
        
     
        

        
