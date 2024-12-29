class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        step 1 : Transpose
        step 2 : Reverse 
        '''
        r = len(matrix)
        c = r # since square matrix

        # for transpose swap the elements around diagonal
        for i in range(r):
            for j in range(i, c):
                matrix[i][j], matrix[j][i]  = matrix[j][i], matrix[i][j]
                
        # reverse each row
        for i in range(r):
            matrix[i].reverse()



        