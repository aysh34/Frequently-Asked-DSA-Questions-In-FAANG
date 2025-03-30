class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        res = []
        for i in range(len(s)):
            mp[s[i]] = i

        i = 0
        while i < len(s):
            end = mp[s[i]]
            
            j = i
            while j < end:
                end = max(end, mp[s[j]])
                j += 1

            res.append(j - i + 1)
            i = j + 1
        return res
