# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left = None
        right = list1
        for i in range(b):
            if i == a-1:
                left = right
            right = right.next
        
        left.next = list2
        curr = list2
        while curr and curr.next:
            curr = curr.next
        
        if curr:
            curr.next = right.next

        return list1