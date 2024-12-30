class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # isk liye mje phele ye tu pta ho k har diagonal k elements konse hain, ek particular diagonal k sary elements ki i-j ki value same hoti hai this is the catch

        m = len(mat)
        n = len(mat[0])

        mp = {} # key/ i-j : value/[diagonal elements]

        for i in range(m):
            for j in range(n):
                if i-j not in mp:
                    mp[i-j] = []
                mp[i-j].append(mat[i][j])

        # now sort the values/diagonals in map
        for i in mp.values():
            i.sort() # or  create a min-heap for each diagonal

        # place elements back in sorted fashion
        for i in range(m-1, -1, -1): # reverse traverse
            for j in range(n-1, -1, -1): 
                mat[i][j] = mp[i-j][-1] # last element of diagonal
                mp[i-j].pop()
        return mat