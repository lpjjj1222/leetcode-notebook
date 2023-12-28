# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#STEP1：用快慢指针找到中点
#STEP2:从中间开始反转后面的链表，切断！
#STEP3:从最左和最右往中间遍历链表
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        #STEP1:
        dummy = ListNode(next=head)
        fast = slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #STEP2:
        cur = slow.next
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        #STEP3:
        left = head
        right = prev
        res = 0
        while left and right:
            res = max(res, left.val+right.val)
            left = left.next
            right = right.next
        return res

        
        
        
