# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode()
        out = output
        while l1 is not None or l2 is not None:
            if l1 is None:
                out.next = ListNode(l2.val, None)
                l2 = l2.next
            elif l2 is None:
                out.next = ListNode(l1.val, None)
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    out.next = ListNode(l1.val, None)
                    l1 = l1.next
                else:
                    out.next = ListNode(l2.val, None)
                    l2 = l2.next
                    
            out = out.next
        # print(l1)
        # print(l2)
        print(output)
        if output.next is None:
            return None
        else:
            
            return output.next