# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        
        times = 1
        while l1:
            num1 += l1.val * times
            l1 = l1.next
            times *= 10

        times = 1
        while l2:
            num2 += l2.val * times
            l2 = l2.next
            times *= 10

        total = num1 + num2

        dummy = ListNode(0)
        cur = dummy

        while total // 10 > 0:
            cur.next= ListNode(total % 10)
            cur = cur.next
            total = total // 10
        cur.next = ListNode(total % 10)
        return dummy.next
            




        

        
