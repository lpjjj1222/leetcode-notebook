class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        words = " ".join(sentence) + " " 
        valid_space = 0
        cnt = 0
        for i in range(rows):
            valid_space += cols
            # 例如i had apple pie的第一行,5%16 = 5,words[5]空格，即had后面是空格，所以说明没被切断
            if words[valid_space % len(words)] == " ":
                valid_space += 1 #加1其实是相当于给第一波words长度-1（最后算的是valid_space // len(words)）,因为另起一行的话，had后面的空格不用了
            # 看下面，其实如果words[valid_space % len(words)-1]是空格的话，也没有被切断，例如，a bcd e第一行， 6%8 = 6,words[6] = e不是空格但是，words[5]
            #是空格，所以第一行也没有切断，这时不用像上面一样valid_space += 1是因为没有省bcd后面的空格
            #如果既不是第一种情况也不是第二种情况， 那word被切断就实锤了
            #被切断就只能像hello world一样8 % 12 = 8, words[8]不是空格，words[7]也不是，-1，valid_space = 7, words[6]也不是，-1,valid_sapce=6
            #words[5]是空格所以不进入While循环，最终valid_space为6
            else:
                while(valid_space > 0 and words[valid_space % len(words) - 1] != " "):
                    valid_space -= 1
        return valid_space // len(words)


        

    
        
