import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        pq = [(grid[0][0], 2 * n - 2, 0, 0)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while pq:
            t, _, r, c = heapq.heappop(pq)
            if (r, c) == (n - 1, n - 1): return t
            for r_inc, c_inc in directions:
                r_, c_ = r + r_inc, c + c_inc
                if 0 <= r_ < n and 0 <= c_ < n and (r_, c_) not in visited:
                    visited.add((r_, c_))
                    heapq.heappush(pq, (max(t, grid[r_][c_]), 2 * (n - 1) - r_ - c_, r_, c_))
        return -1
