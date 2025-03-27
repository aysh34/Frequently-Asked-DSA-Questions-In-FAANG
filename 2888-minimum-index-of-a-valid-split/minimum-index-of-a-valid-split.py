class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
    # dominant element using Boyer-Moore Voting Algorithm
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        total_count = nums.count(candidate)
        
        left_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                left_count += 1
            right_count = total_count - left_count
            
            # if both left and right subarrays satisfy the dominance condition
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - i - 1):
                return i  # Minimum index satisfying the condition
        
        return -1 