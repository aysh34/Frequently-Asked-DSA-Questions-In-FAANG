class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i in range(len(nums)):
            if nums[i] in mp:
                if abs(mp[nums[i]] - i) <= k:
                    return True
            # weather the current element is not in the map or abs(i-j) <= k condition doesn't met update mp[nums[i]] to this new index i
            mp[nums[i]] = i
        return False
