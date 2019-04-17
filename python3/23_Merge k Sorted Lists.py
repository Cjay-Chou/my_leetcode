# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while None in lists:
            lists.remove(None)
        if len(lists) is 0:
            return None
        result = ListNode(0)
        temp = result
        
        while lists:
            minnum = lists[0].val
            target = 0
            for num in range(len(lists)):
                if lists[num].val <= minnum:
                    minnum = lists[num].val
                    target = num
                    
            if lists[target].next != None:
                temp.next = lists[target]
                lists[target]=lists[target].next
                temp = temp.next
            else:
                temp.next = lists[target]
                temp = temp.next
                del lists[target]
                        
        return result.next