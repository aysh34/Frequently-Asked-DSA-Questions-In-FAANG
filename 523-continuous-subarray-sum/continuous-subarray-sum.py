class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        s = 0

        for i in range(len(nums)):
            s += nums[i]

            if s%k in mp:
                if i - mp[s%k] >= 2:
                    return True
            else:
                mp[s%k] = i
        return False
