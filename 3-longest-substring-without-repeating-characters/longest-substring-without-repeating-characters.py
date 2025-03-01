class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx = 0
        seen = []
        for i in s:
            if i not in seen:
                seen.append(i)
            else:
                mx = max(mx, len(seen))
                idx = seen.index(i)
                seen = seen[idx+1:]  # Duplicate ke baad ka portion rakho
                seen.append(i)       # Current character ko dubara add karo
        
        return  max(mx, len(seen))