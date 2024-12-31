class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        mp = {}
        res = []

        for i in changed: # populate map
            if i not in mp:
                mp[i] = 0
            mp[i] += 1

        for j in changed:
            if mp[j] == 0: # freq = 0 so skip
                continue
            if mp.get(j * 2, 0) == 0:  # If double of i is not available, return []
                return []


            # otherwise we've found the twice so append the num
            res.append(j)
            mp[j] -= 1
            mp[j*2] -= 1
        return res