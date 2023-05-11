# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        #basecase 两个链的head相等
        if headA == headB:
            return headA


        #求出两个链表的长度差，然后让长的那个链的指针移动到短链开始的地方，
        #两指针就可以同时移动并对比是否相等了

        length_a,length_b = 1,1
        cur_a, cur_b = headA, headB

        #求出两个链表的长度差
        while cur_a.next:
            length_a += 1
            cur_a = cur_a.next

        while cur_b.next:
            length_b += 1
            cur_b = cur_b.next

        length_diff = abs(length_a - length_b)
        
        #看谁长谁短
        if length_a > length_b:
            long_list, short_list = headA, headB

        elif length_a <= length_b:
            long_list, short_list = headB, headA
        

        #让长的那个链的指针移动到短链开始的地方
        for _ in range(length_diff):
            long_list = long_list.next

        #同时移动比较是否相等
        while long_list.next:
            if long_list == short_list:
                return long_list
            long_list, short_list = long_list.next, short_list.next

        #判断最后一个node,因为最后一个node已经不能在while循环里
        if long_list == short_list:
            return long_list
        else:
            return None


                

