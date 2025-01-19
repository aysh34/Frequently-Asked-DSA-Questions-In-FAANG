# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def merge2Lists(l1,l2): # return 1 sorted list
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val < l2.val:
                l1.next = merge2Lists(l1.next,l2) # l1 tu fix ho gya ab uska next kiya ho ga ye recursively decide ho ga
                return l1
            else:
                l2.next = merge2Lists(l1,l2.next)
                return l2
                
        first = lists[0]
        for i in range(1,len(lists)):
            first = merge2Lists(first,lists[i])
        return first
