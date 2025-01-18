import random
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        temp = head
        while temp:
            self.arr.append(temp.val)
            temp = temp.next

    def getRandom(self) -> int:
        idx = random.randint(0,len(self.arr)-1)
        return self.arr[idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()