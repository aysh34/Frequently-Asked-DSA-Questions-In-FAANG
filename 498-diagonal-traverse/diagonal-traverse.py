class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # i + j for this direction↗ traversal

        m = len(mat)
        n = len(mat[0])
        mp = {}
        for i in range(m):
            for j in range(n):
                if i+j not in mp:
                    mp[i+j] = []
                mp[i+j].append(mat[i][j])
        
        res = []
        values = list(mp.values()) # extract all lists

        for i in range(len(values)):
            if i % 2 == 0:
                res.extend(values[i][::-1]) # Iterates through the object (list) and adds each element to the target list.
            else:
                res.extend(values[i])

        return res