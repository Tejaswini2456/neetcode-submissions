class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        components = 0
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        for node in range(n):
            if node in visited:
                continue
            components += 1
            dfs(node)
        return components        