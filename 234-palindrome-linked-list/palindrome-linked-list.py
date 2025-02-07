# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next

        # l = 0
        # r = len(arr)-1
        # while l < r:
        #     if arr[l] != arr[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        # 2nd approach: reverse and find middle in one pass
        # if not head or not head.next:
        #     return True

        # slow = fast = head
        # prev = None
        # while fast and fast.next:
        #     fast = fast.next.next
        #     temp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = temp 

        # if fast != None: # odd no of nodes 
        #     slow = slow.next # skip middle unique node 

        # while prev and slow:
        #     if prev.val != slow.val:
        #         return False
        #     prev = prev.next
        #     slow = slow.next
        # return True

        # 3rd approach
        curr = head
        def recur(head):
            nonlocal curr
            if head == None:
                return True
            ans = recur(head.next)
            # now head will be pointing to the last node
            if head.val != curr.val:
                return False
            curr = curr.next
            return ans
        return recur(head)