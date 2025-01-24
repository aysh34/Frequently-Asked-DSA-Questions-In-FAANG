# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first reverse both of the lists
        def reverseList(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev
        
        r_l1  =  reverseList(l1)
        r_l2  =  reverseList(l2)

        dummy = ListNode(0)
        curr = dummy
        carry = 0       

        while r_l1 or r_l2 or carry:
            v1 = r_l1.val if r_l1 else 0
            v2 = r_l2.val if r_l2 else 0

            sum_values = v1 + v2 + carry
            digit = sum_values % 10
            carry = sum_values // 10
            curr.next = ListNode(digit)
            curr = curr.next

            r_l1 = r_l1.next if r_l1 else None
            r_l2 = r_l2.next if r_l2 else None

        
        return reverseList(dummy.next)