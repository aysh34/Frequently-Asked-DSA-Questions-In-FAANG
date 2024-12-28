class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = float("inf")
        for i in range(n-2):  # fix one no
            l = i + 1 # two pointer approach
            r = n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                if curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest

        # n = len(nums)
        # closest = float('inf') # very large +ve no
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1,n):
        #             curr_sum = nums[i] + nums[j] + nums[k]

        #             if abs(target - curr_sum) < abs(target - closest):
        #                 closest = curr_sum
        # return closest    # this approach gives you TLE
