class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 1
        
        left = 0
        bits = 0
        
        for right in range(n):
            while bits & nums[right] != 0:
                bits ^= nums[left]
                left += 1
                
            bits |= nums[right]
            
            max_length = max(max_length, right - left + 1)
            
        return max_length
        
        