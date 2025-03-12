class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        mx = float('-inf')
        pos = 0
        neg = 0

        for i in nums:
            if i < 0:
                neg += 1
            if i > 0:
                pos += 1
            
            mx = max(pos,neg)
        return mx
