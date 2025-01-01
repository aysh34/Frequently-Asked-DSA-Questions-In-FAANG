class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            # pehle har index ka left sum or right sum check krlo jiska ye dono same hu wahi answer ho ga otherwise es current element ko left sum mei add krdo or agy barh jao next element ko dekho
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return -1      
