"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None 

        newHead = None
        prev = None
        curr = head
        mp = {}
        while curr:
            newNode = Node(curr.val) # newNode create 
            mp[curr] = newNode # store 

            if newHead == None: # start 
                newHead = newNode
                prev = newHead
            else: # list is already created
                prev.next = newNode
                prev = newNode # to keep previous updated
        
            curr = curr.next 

        curr = head
        newCurr = newHead

        while curr:
            if curr.random == None:
                newCurr.random = None
            else:
                newCurr.random = mp[curr.random]
            curr = curr.next
            newCurr = newCurr.next

        return newHead