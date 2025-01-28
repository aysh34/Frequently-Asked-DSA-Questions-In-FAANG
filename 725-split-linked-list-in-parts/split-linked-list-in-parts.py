# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int):
        if not head:
            return [None] * k
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        # total parts = k
        eachPartNodes = l // k
        extraNodes = l % k 

        res = [None for _ in range(k)] # k no of lists 
        curr = head
        for i in range(k):
            res[i] = curr
            # now fill each part
            for j in range(eachPartNodes + ( 1 if extraNodes > 0 else 0)):
                prev = curr
                curr = curr.next
            
            if prev:
                prev.next = None

            extraNodes -= 1

        return res       