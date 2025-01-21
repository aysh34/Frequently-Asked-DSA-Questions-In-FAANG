class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row1SumRemainingForR2 = sum(grid[0])
        row2SumRemainingForR2 = 0

        minimizedforR2 = float('inf')

        for i in range(len(grid[0])):
            row1SumRemainingForR2 -= grid[0][i] # R1 moves
            bestForR2 = max(row1SumRemainingForR2, row2SumRemainingForR2)
            minimizedforR2 = min(minimizedforR2,bestForR2)
            row2SumRemainingForR2 += grid[1][i]
        return minimizedforR2