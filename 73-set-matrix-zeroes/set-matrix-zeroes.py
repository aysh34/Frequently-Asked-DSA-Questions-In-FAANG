class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        rSet = set()
        cSet = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rSet.add(r)
                    cSet.add(c)
        
        for r in rSet:
            for c in range(cols):
                matrix[r][c] = 0

        for r in range(rows):
            for c in cSet:
                matrix[r][c] = 0
