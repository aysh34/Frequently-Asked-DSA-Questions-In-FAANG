class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows = len(matrix)
        cols = len(matrix[0])

        res = []
        """
        direction 0: left to right
            constant : row / top
        direction 1: top to bottom
            constant : column / right 
        direction 2: right to left
            constant : row / bottom
        direction 3: bottom to top
            constant : column / left
        """
        top = 0
        right = cols - 1  # idx of last col = no of cols - 1
        left = 0
        bottom = rows - 1  # idx of last row

        dir = 0
        while top <= bottom and left <= right:
            if dir == 0:
                for i in range(left, right + 1):  # move left to right
                    res.append(matrix[top][i])  #  top is constant
                top += 1  # move top downwards after the whole row gets print

            elif dir == 1:
                for i in range(top, bottom + 1):  # move top to bottom
                    res.append(matrix[i][right])  # constant = right col
                right -= 1  # move right towards left side

            elif dir == 2:
                for i in range(right, left - 1, -1):  # move from right to left
                    res.append(matrix[bottom][i])  # bottom row is constant
                bottom -= 1  # move bottom upwards

            elif dir == 3:
                for i in range(bottom, top - 1, -1):  # move from bottom to top
                    res.append(matrix[i][left])  # left col is constant
                left += 1  # move left towards right side

            dir = (
                dir + 1
            ) % 4  #  way to ensure the dir variable cycles through the values 0, 1, 2, 3 in a circular manner

        return res
