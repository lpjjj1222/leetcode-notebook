# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #对于判断链表是否是环形，用快慢指针，快的每次走两步，慢的每次走一步
        #如果是环形的，总会碰上

        #因此这个问题，也想到用快慢指针解决
        #但是这个问题太tm变态了要找环形入口
        #看代码随想录吧！还要设计x y z 变量！
        #但是懂了之后很好理解

        #看懂来这
        #首先排除tmd head就是None这种傻逼

        #step1:先找到相遇的点

        fast,slow = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:  
        #step2:一个点从相遇点出发，另一个从head出发，每次走一步
                meet_node = fast
                start_node = head

                while meet_node != start_node:
                    meet_node = meet_node.next
                    start_node = start_node.next
                return start_node
        return None


                    
  

