class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # one way is to sort each string

        mp = {}

        for i in strs:
            s = "".join(sorted(i))
            if s not in mp: # if key is not present
                mp[s] = []
            mp[s].append(i) # append current string weather key is or is not 

            
        
        return list(mp.values())