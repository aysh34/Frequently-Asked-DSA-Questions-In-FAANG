class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of 1st n natural numbers = n*(n+1)/2
        n = len(nums)
        sum = n*(n+1)//2
        for i in nums:
            sum -= i
        return sum

        
        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     if i != nums[i]:
        #         return i
        # return n