class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minDist = [float("inf")] * n
        visited = [False] * n
        minDist[0] = 0
        totalCost = 0
        for _ in range(n):
            curr = -1
            for i in range(n):
                if not visited[i] and(curr == -1 or minDist[i] < minDist[curr]) :
                    curr = i
            visited[curr] = True
            totalCost += minDist[curr]
            x1,y1 = points[curr]
            for i in range(n):
                if not visited[i]:
                    x2,y2 = points[i]
                    cost = abs(x1-x2) + abs(y1-y2)
                    minDist[i] = min(minDist[i],cost)
        return totalCost
        