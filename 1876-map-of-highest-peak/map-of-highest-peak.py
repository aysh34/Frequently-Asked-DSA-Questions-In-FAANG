from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        height = [[-1] *  n for _ in range(m)] # step 1

        # step 2: add all source nodes/water cells to queue
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1: # mtlb water cell
                    height[i][j] = 0
                    q.append((i,j))

        # step 3: Multi Source BFS
        directions = [(0,1),(0,-1),(1,0),(-1,0)] 
        while q:
            i , j = q.popleft()
            # ab is cur i,j se 4 directions mei ja skty hain
            for x,y in directions:
                new_i = i + x
                new_j = j + y

                if 0 <= new_i < m and 0 <= new_j < n and height[new_i][new_j] == -1: # not visited
                    height[new_i][new_j] = height[i][j] + 1
                    q.append((new_i,new_j))

        return height