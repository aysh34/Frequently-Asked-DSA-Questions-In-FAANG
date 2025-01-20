# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1 pass approach
        temp = head
        p1 = None
        p2 = None

        while temp:
            if p2 != None:
                p2 = p2.next

            k -= 1
            if k == 0:
                p1 = temp
                p2 = head
            temp = temp.next
       
        p1.val, p2.val = p2.val, p1.val 
        return head

        # l = 0
        # temp = head
        # while temp:
        #     l += 1
        #     temp = temp.next

        # if k > l or k <= 0:
        #     return head

        # node1 = head
        # for i in range(k - 1):
        #     node1 = node1.next

        # node2 = head
        # for i in range(l - k):
        #     node2 = node2.next

        # node1.val, node2.val = node2.val, node1.val
        # return head
