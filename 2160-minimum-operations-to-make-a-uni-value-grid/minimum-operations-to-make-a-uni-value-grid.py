class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        first_mod = grid[0][0] % x
        l = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] % x != first_mod:
                    return -1
                l.append(grid[i][j])

        l = sorted(l)
        median = l[len(l) // 2]

        operations = 0
        for i in l:
            operations += abs(i - median) // x
        
        return operations