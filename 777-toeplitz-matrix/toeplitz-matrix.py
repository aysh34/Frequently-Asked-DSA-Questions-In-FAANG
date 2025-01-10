class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
