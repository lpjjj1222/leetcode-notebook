# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #看是否整个链表小于k个
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next
        
        #翻转一组
        prev = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        #前面翻转完第一组后，head就在这一组的末尾了，要翻转下一组，只需要递归
        #而翻转完上一组后，cur已经在新的一组的第一个
        head.next = self.reverseKGroup(cur, k)
        return prev
