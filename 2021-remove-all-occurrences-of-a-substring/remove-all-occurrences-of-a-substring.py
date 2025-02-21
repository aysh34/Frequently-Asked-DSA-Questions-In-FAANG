class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""

        for i in range(len(s)):
            res += s[i]
            if len(res) >= len(part):
                startIdx = len(res) - len(part)
                if res[startIdx:] == part:
                    res = res.replace(res[startIdx:],"")
        return res