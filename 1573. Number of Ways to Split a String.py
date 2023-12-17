class Solution:
    def numWays(self, s: str) -> int:
        #第一种可能，整个s中1的数量不能被3整除，则搞不了
        #第二种可能，没有1在s里，分成三份就相当于在n个0之间的n-1个间隙中选两个间隙分成三份 即从(n-1)选2个的排列数，公式计算得(n-1)*(n-2)/2
        #第三种可能，1的数量可以被3整除，假设为each_block_n,那么遍历到1的数量为each_block_n的index后面就可以开始切，一直到遇到下一个1.然后重新计算1的个数，又达到each_block_n的Index后面可以开始切直到下一个1。

        n = s.count("1")
        print("n=",n)
        

        if n % 3 != 0:
            return 0
        elif n == 0:
            m = s.count("0")
            return int((m-1) * (m-2) / 2) % (10**9 + 7)
        else:
            each_block_n = int(n/3)
            count_1 = first_p = second_p =  0

            for num in s:
                if num == "1":
                    count_1 += 1
                if count_1 == each_block_n:
                    first_p += 1
                elif count_1 == each_block_n * 2:
                    second_p += 1

            return first_p * second_p % (10**9 + 7)
