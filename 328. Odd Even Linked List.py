# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd_cur = head
        even_cur = head.next
        even_head = head.next
        #用同时串联奇数偶数不然会后处理的时候就会乱
        while even_cur and even_cur.next:
            odd_cur.next = even_cur.next
            odd_cur = odd_cur.next
            even_cur.next = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even_head
        return head


        


        
