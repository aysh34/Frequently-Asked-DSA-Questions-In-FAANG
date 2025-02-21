class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = 0  # stores unique no at the end
        for n in nums:
            res = res ^ n  # result XOR current_no
        return res


# why this works: repeated numbers cancel out because X ⊕ X = 0