# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        temp = l3
        up = 0
        while l1 is not None and l2 is not None:
            temp.next = ListNode(0)
            temp = temp.next
            temp.val = (l1.val+l2.val+up)%10
            up = (l1.val+l2.val+up)//10
            l1 = l1.next
            l2 = l2.next
        
        while l1 is not None:
            temp.next = ListNode(0)
            temp = temp.next
            temp.val = (l1.val+up)%10
            up = (l1.val+up)//10
            l1 = l1.next
        
        while l2 is not None:
            temp.next = ListNode(0)
            temp = temp.next
            temp.val = (l2.val+up)%10
            up = (l2.val+up)//10
            l2 = l2.next
        if up == 1:
            temp.next = ListNode(1)
        
        return l3.next
        