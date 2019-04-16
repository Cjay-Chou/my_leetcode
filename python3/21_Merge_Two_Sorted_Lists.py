# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        temp = l3
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
        
        if l1 == None:
            temp.next = l2
        else:
            temp.next = l1
            
        return l3.next
                