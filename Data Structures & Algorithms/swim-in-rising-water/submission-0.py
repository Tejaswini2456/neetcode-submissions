class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0],0,0)]
        visited = set()
        time = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while minHeap:
            elevation,r,c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            time = max(time,elevation)
            if r == n-1 and c == n-1:
                return time
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if (0 <= nr <= n-1 and 0 <= nc <= n-1 and (nr,nc) not in visited):
                    heapq.heappush(
                        minHeap,(grid[nr][nc],nr,nc)
                    )
        