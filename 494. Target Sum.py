#他吗了个比绝对不能看代码随想录
#直接看哥下面的东西就行了！！！！！
#代码随想录视频用一维数组做，根本讲不清楚！用二维数组做！！！
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #正数的和加起来为Add, 负数的和加起来为Minus
        #正数-负数 = target 即 Add - Minus = Target ① 
        #正数＋负数 = sum(nums) 即 Add + Minus = sum(nums) ②
        #将①②两式子相加，得到2Add = Target + sum(nums)
        
        #如果nums每个数的绝对值都小于target的绝对值，就搞不了
        abs_nums_sum = sum([abs(num) for num in nums])
        abs_target = abs(target)
        if abs_nums_sum < abs_target:
            return 0

        #如果Add得出不为整数，则无法实现，返回0种方法
        if (target + sum(nums)) % 2 != 0:
            return 0
        else:
            Add = int((target + sum(nums)) / 2)
        #本题转化为，从nums序列的物品中，（value = weight）,有几种方法能把容量为Add的背包填满
        #所以dp[i][j]表示从序列为[0,1]的物品种任选，将容量为j的背包填满一共有几种方法

        #创建数组
        dp = [[0] * (Add+1) for _ in range(len(nums))]
        #初始化数组
        #第一行（遍历第一个物品的时候）只有书包容量刚好等于第一个物品的重量才能刚好放满，即一种方法 其他容量都是0种方法
        for j in range(Add+1):
            if j == nums[0]: #如果书包容量刚刚好为第一个物品的容量
                dp[0][j] = 1
        #如果在nums序列中有0,0的前面可以加正号或者负号，而且分别算一种方法，所以第一列，即书包容量为0的时候，要去看nums序列里的前i个元素有几个零，有几个，方法就是2的几次方
        #有一个奇怪的地方是，如果零的个数是0的话，2的0次方是1 （不管它，直接过了，也没找到合适能说明白的说法...代码随想录里硬讲成书包容量为0，只有一种方法就是不放东西...呃）
        for i in range(len(nums)):
            count = 0
            for index in range(i+1):
                if nums[index] == 0:
                    count += 1
            dp[i][0] = 2 ** count


        #eg. 物品序列为[①，②，③] 背包容量为j

        #从上一行走到下一行。 遍历到i物品，如果不拿i, 则dp[i][j]= dp[i-1][j]，即跟遍历i-1的时候方法一样
        #如果拿i,则dp[i][j] = dp[i-1][j-weight[i]]
        #拿和不拿两种情况加起来，就是遍历到i物品的总情况，即dp[i][j] = dp[i-1][j] + dp[i-1][j-weight[i]]
        for i in range(1,len(nums)):
            for j in range(Add+1):
                if j < nums[i]:
                #如果书包剩下的容量已经放不下i物品了，就只有不放i的选择了
                    dp[i][j] = dp[i-1][j]
                else:
                #如果书包容量允许：
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        return dp[len(nums) - 1][Add]
        



        
