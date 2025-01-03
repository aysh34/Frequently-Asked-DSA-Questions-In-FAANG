class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # since we need largest perimeter so we should sort the array
        nums.sort()

        for i in range(len(nums)-1 , 1 , -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]

        return 0