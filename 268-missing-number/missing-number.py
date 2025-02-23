class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res = (res ^ i) ^ nums[i]
        return res


        # sum of 1st n natural numbers = n*(n+1)/2
        # n = len(nums)
        # sum = n*(n+1)//2
        # for i in nums:
        #     sum -= i
        # return sum # O(n)


        # n = len(nums)
        # nums.sort() (n log n)
        # for i in range(n):
        #     if i != nums[i]:
        #         return i
        # return n