class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        count = 0

        def dfs(node, nodes):
            stack = [node]
            visited.add(node)
            nodes.add(node)
            while stack:
                curr = stack.pop()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
                        nodes.add(neighbor)

        for i in range(n):
            if i not in visited:
                nodes = set()
                dfs(i, nodes)
                # A complete component must have |nodes| connections for each node
                if all(len(graph[node]) == len(nodes) - 1 for node in nodes):
                    count += 1

        return count


        # graph = {i: {i} for i in range(n)}
        
        # for u, v in edges:
        #     graph[u].add(v)
        #     graph[v].add(u)
        
        # # Count complete components
        # component_sizes = Counter(map(frozenset, graph.values()))
        # return sum(len(comp) == size for comp, size in component_sizes.items())
