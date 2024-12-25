class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #           return [i,j]
        #  TC: O(n2)
        #  TC: O(1)

        map = {}  # value:index
        for i in range(0, len(nums)):
            remaining = target - nums[i]
            if remaining in map:
                return [map[remaining], i]
            else:
                map[nums[i]] = i


# TC: O(n)
