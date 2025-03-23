import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = {i: [] for i in range(n)}

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Min-heap: (distance, node)
        min_heap = [(0, 0)]  # Start from node 0 with distance 0
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if time > dist[node]:
                continue  

            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time

                if new_time < dist[neighbor]:  # Found a shorter path
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(min_heap, (new_time, neighbor))
                
                elif new_time == dist[neighbor]:  # Found an equally short path
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n-1]
