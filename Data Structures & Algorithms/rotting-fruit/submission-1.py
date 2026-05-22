class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        def bfs(q):                    
            nonlocal fresh
            time = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q and fresh:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if (0 <= r < rows and
                            0 <= c < cols and
                            grid[r][c] == 1):
                            grid[r][c] = 2
                            fresh -= 1
                            q.append((r, c))
                time += 1
            return time

        for r in range(rows):          
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        time = bfs(q)
        return time if fresh == 0 else -1