class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        maxLen = 0
        maxFreq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq = max(maxFreq, count[s[right]])

            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen