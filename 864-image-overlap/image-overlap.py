class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)

        def count_max_overlap(row_off, col_off):
            count = 0
            for i in range(n):
                for j in range(n):
                    # A = fixed, B = move, B ka offset nikalo from A
                    b_i = i + row_off
                    b_j = j + col_off

                    if b_i < 0 or b_i >=n or b_j < 0 or b_j >= n:
                        continue
                    if A[i][j] == 1 and B[b_i][b_j] == 1:
                        count += 1
            return count

        max_overlap = 0
        for row_off in range(-n+1,n): 
            # har ek row offset k liye sare col offset try kro
            for col_off in range(-n+1,n):
                count = count_max_overlap(row_off,col_off)
                max_overlap = max(max_overlap,count)

        return max_overlap
