class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = { i: [] for i in range(1,n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
        minHeap = [(0,k)]
        dist = {}
        while minHeap:
            time,node = heapq.heappop(minHeap)
            if node in dist:
                continue
            dist[node] = time
            for neighbor,weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(minHeap,(time+weight,neighbor))
        return max(dist.values()) if len(dist) == n else -1