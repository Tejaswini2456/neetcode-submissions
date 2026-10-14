class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)
        for src in adj:
            adj[src].sort(reverse=True)
        route = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            route.append(src)
        dfs("JFK")
        return route[::-1]