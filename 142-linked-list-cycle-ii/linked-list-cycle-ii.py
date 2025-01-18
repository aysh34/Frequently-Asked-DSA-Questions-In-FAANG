# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None
        # now find start of the cycle, reset one pointer to head
        slow = head
        while slow != fast:  # where both gets equal that's the start of the cycle
            slow = slow.next
            fast = fast.next

        return slow