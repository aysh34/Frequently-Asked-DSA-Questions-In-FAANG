class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1  # Add character to window
            
            while all(count[ch] > 0 for ch in "abc"):  # Check if all 'a', 'b', 'c' exist
                count[s[left]] -= 1  # Shrink window from left
                left += 1
            res += left  # Count valid substrings

        return res
        # c = 0
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)+1):
        #         sub = s[i:j]
        #         if 'a' in sub and 'b' in sub and 'c' in sub:
        #             c += 1
        # return c