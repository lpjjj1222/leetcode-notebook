#!/usr/bin/env python
# coding: utf-8

# In[124]:


def numRescueBoats(people,limit):
#对撞指针最经典的题目就是14579逐渐增大的数列，找相加=12的两两数对
#放到这里，就很像啊！ 两个人体重之和 <=limit

#由于people这个list无序，所以先排序
    people.sort()

    #左指针 和 右指针 以及船的数量
    left = 0
    right = len(people) - 1
    boats = 0


    #当左右指针还没对撞时，进入While循环
    while left <= right:

            #无论左指针和右指针的体重之和是否大于limit,右指针都要往左,且船都要用掉一艘
            #因为如果大于limit,则右指针体重自己乘船，右指针往左和原来的左指针加起来和limit对比
            #如果小于limit,则直接左右指针一起乘船，右指针往左，左指针往右
        if left != right and people[right] + people[left] <= limit:
            left += 1

        boats += 1
        right -= 1

    return boats


# In[125]:


numRescueBoats([7,8],8)


# In[ ]:


#下面的是递归，刷题最好不用递归，因为时间和空间复杂度都不太行


# In[79]:


def numRescueBoats(people, limit):
        #对撞指针最经典的题目就是14579逐渐增大的数列，找相加=12的两两数对
    #放到这里，就很像啊！ 两个人体重之和 <=limit
    
    #由于people这个list无序，所以先排序
    people.sort()

    #注意这题people里的所有元素都小于等于limit

    #注意对撞指针的题目由于要考虑到对撞，因此每一个index必须唯一，所以不能把元素remove出列表，也不要把右指针的最开始定义为people[-1]

    def howmanyboats(right_index,left_index):
        #如果people列表里只有一个数字，则一上来就会对撞
        if right_index == left_index:
            return 1

        #如果右指针对应的数刚好等于limit,则自己上一艘船，并将右指针往左移
        if people[right_index] == limit:
            return 1 + howmanyboats(right_index -1,left_index)

        #如果左指针对应的数刚好等于limit,则自己上一艘船，并将左指针往右移
        if people[left_index] == limit:
            return 1 + howmanyboats(right_index, left_index + 1)

        #如果左右指针对应的数相加 < limit,则一起上一艘船， 左右指针分别移一格
        if people[left_index] + people[right_index] <= limit:
            #如果下一步就要对撞，例如[1,2],limit = 3, 应该直接结束递归
            if left_index + 1 == right_index:
                return 1
            else:
                return 1 + howmanyboats(right_index -1, left_index +1)

        #如果左右指针对应的数相加 > limit, 则把右指针向左移，使两数之和变小，且右指针对应的数上船
        #上船是因为把最小的搭给他都不能一起坐船，只能自己坐

        if people[left_index] + people[right_index] > limit:
            #如果即将对撞，即[4,5],limit = 6,则应各上一条船，且结束递归
            if left_index + 1 == right_index:
                return 2
            else:
                return 1 + howmanyboats(right_index -1, left_index)
            
    return howmanyboats(len(people)-1,0)

    
    
    
    
        

