# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list_length = 0
        out = head
        temp = head
        while temp is not None:
            temp = temp.next
            list_length += 1
            
        k = list_length - n
        
        left = head
        right = left.next
        if k == 0:
            return right
        while k > 1:
            left = left.next
            right = right.next
            k -= 1
            
        if right is None:
            return head
        left.next = right.next
        
        
            
        
        return out