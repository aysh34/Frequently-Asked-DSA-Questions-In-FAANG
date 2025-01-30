# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # left and right are 1-based indices
        if not head or left == right:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        # prev ko left - 1 tk le ao
        for i in range(left - 1):
            prev = prev.next

        # prev --> one node before the reversal part
        curr = prev.next  # start node of the reversal part

        # now we just have to traverse right-left to reverse the specific part
        for i in range(right - left):
            temp = curr.next 
            curr.next = temp.next # not curr.next.next
            temp.next = prev.next # not curr
            prev.next = temp
        return dummy.next
