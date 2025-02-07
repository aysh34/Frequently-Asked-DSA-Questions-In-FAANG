class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorCountMap = {}  # color:count
        ballColorMap = {}   # ballno:color
        res = []
        for i in range(len(queries)):
            ballNo = queries[i][0]
            color = queries[i][1]

            # is ball ko isk color k sth ballColorMap mei dalna hai but first check if it already colored?
            if ballNo in ballColorMap:
                prevColor = ballColorMap[ballNo]

                # erase this prevColor from colorCountMap
                colorCountMap[prevColor] -= 1
                if colorCountMap[prevColor] == 0:
                    colorCountMap.pop(prevColor)

            ballColorMap[ballNo] = color # new color
            colorCountMap[color] = colorCountMap.get(color,0) + 1
            res.append(len(colorCountMap))

        return res