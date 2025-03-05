from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26 # s2 ka current window ka character count store karega

        # Initialize frequency counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Slide the window over s2
        for i in range(len(s2) - len(s1)):
            if s1Count == s2Count:
                return True
            s2Count[ord(s2[i]) - ord('a')] -= 1 # shrink window (remove left character)
            s2Count[ord(s2[i + len(s1)]) - ord('a')] += 1 # Expand Window (Add new character)

        # Check the last window
        return s1Count == s2Count

        # 2nd approach
        # s1 = sorted(s1)
        # n = len(s1)

        # for i in range(len(s2)-n+1):
        #     portion = sorted(s2[i:i+n])
        #     if s1 == portion:
        #         return True
        # return False