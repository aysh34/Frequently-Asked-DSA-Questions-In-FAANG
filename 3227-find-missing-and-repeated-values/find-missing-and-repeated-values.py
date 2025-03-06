class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mp = {}
        n = len(grid)
        arr = [i for i in range(1,n**2+1)]
        res = [None] * 2
        for i in range(n):
            for j in range(n):
                mp[grid[i][j]] = mp.get(grid[i][j],0) + 1
        
        for i in arr:
            if i in mp and mp[i] > 1:
                res[0] = i
            if i not in mp:
                res[1] = i
        return res