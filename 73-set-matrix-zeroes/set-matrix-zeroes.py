class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # without extra space
        rows = len(matrix)
        cols = len(matrix[0])
        
        first_col_zero = False

        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
            
            for c in range(1, cols):  # first column isn't affected yet
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # Mark row
                    matrix[0][c] = 0  # Mark column

        # Use markers to set rows & cols to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0: # handle first row
            for c in range(cols):
                matrix[0][c] = 0

        if first_col_zero: # handle first column
            for r in range(rows):
                matrix[r][0] = 0

        

        # rows = len(matrix)
        # cols = len(matrix[0])
        # rSet = set()
        # cSet = set()
        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == 0:
        #             rSet.add(r)
        #             cSet.add(c)
        
        # for r in rSet:
        #     for c in range(cols):
        #         matrix[r][c] = 0

        # for c in cSet:
        #     for r in range(rows):
        #         matrix[r][c] = 0 # SC = O(m + n)
