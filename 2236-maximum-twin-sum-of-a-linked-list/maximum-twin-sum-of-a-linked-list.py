# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        firstHalf = head
        secondHalf = prev 
        maxTwinSum = float('-inf')

        while secondHalf:
            maxTwinSum = max(maxTwinSum,firstHalf.val + secondHalf.val)
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
           
        return maxTwinSum

        # arr = []

        # temp = head
        # while temp:
        #     arr.append(temp.val)
        #     temp = temp.next

        # maxTwinSum = float('-inf')
        # n = len(arr)
        # for i in range(n):
        #     twinIndex = n-1-i
        #     maxTwinSum = max(maxTwinSum,arr[i] + arr[twinIndex])
        
        # return maxTwinSum
