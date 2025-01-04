class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = mis = -1

        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0: # already visit
                dup = abs(nums[i])
            else:
                nums[abs(nums[i]) - 1] *= - 1 # Mark -1 as visited
        
        for i in range(n):
            if nums[i] > 0: # positive hai
                mis = i + 1
                break 
        return [dup,mis] 