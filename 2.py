# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # print(l1)
        # print(l2)
        out = ListNode()
        pointer = out
        # print(out)
        carry = 0
        while l1 or l2 or carry:
            print(out)
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
                
            # l1_val = 0 if not l1 else l1.val
            # l2_val = 0 if not l2 else l2.val
            curr_val = l1_val + l2_val + carry
            if curr_val >= 10:
                curr_val -= 10
                carry = 1
            else:
                carry = 0
            pointer.val = curr_val
            if l1 or l2 or carry:
                pointer.next = ListNode()
                pointer = pointer.next
        return out
            