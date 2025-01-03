class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                if abs(mp[nums[i]] - i) <= k:
                    return True
# weather the current element is not in the map or is present in map but the condition abs(i-j) <= k doesn't met update the value of key/current no in map to this new/latest index i            
            mp[nums[i]] = i
        return False
