from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0: 
            return []

        changed.sort() 
        mp = Counter(changed)  # Frequency map for changed array
        res = []

        for num in changed:
            if mp[num] == 0:  # If freq = 0, skip it
                continue
            if mp[num * 2] == 0:  # If double of the number doesn't exist, return []
                return []

            # otherwise we've found its twice so decrease their frequencies
            res.append(num)
            mp[num] -= 1
            mp[num * 2] -= 1

        return res
